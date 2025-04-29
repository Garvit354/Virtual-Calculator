import cv2
from cvzone.HandTrackingModule import HandDetector

class Button :
    def __init__(self,position,width,height,value):
        self.position =position
        self.width =width
        self.height =height
        self.value =value

    def draw(self,img):
        cv2.rectangle(img, self.position, (self.position[0]+self.width, self.position[1]+self.height), (200, 200, 200), cv2.FILLED)
        cv2.rectangle(img, self.position, (self.position[0] + self.width, self.position[1] + self.height),
                      (100, 100, 100), 3)
        cv2.putText(img, self.value, (self.position[0] + 30, self.position[1] + 67), cv2.FONT_HERSHEY_DUPLEX,
                    2, (100, 100, 100), 2)

    def clickCheck(self,x,y,img):

            if self.position[0] < x <self.position[0] + self.width and self.position[1] < y <self.position[1] + self.height:
                cv2.rectangle(img, self.position, (self.position[0] + self.width, self.position[1] + self.height),
                              (255, 255, 255), cv2.FILLED)
                cv2.rectangle(img, self.position, (self.position[0] + self.width, self.position[1] + self.height),
                              (100, 100, 100), 3)
                cv2.putText(img, self.value, (self.position[0] + 15, self.position[1] + 78), cv2.FONT_HERSHEY_DUPLEX,
                            3, (50, 50, 50), 3)
                return True
            else:
                return False

# webCam
cap = cv2.VideoCapture(0)
cap.set(3,1280)
cap.set(4,720)

#hand detection
detector = HandDetector(detectionCon=0.8, maxHands=1)

buttonListValue=[['C','(',')','%'],
                 ['7','8','9','*'],
                 ['4','5','6','-'],
                 ['1','2','3','+'],
                 ['0','/','.','=']]

buttonList=[]
for y in range(5):
    for x in range(4):
        xpos = x * 100 +800
        ypos = y * 100 + 150
        buttonList.append(Button((xpos, ypos),100,100,buttonListValue[y][x]))

myEquation =''
delayCounter = 0

while True:

    success, img = cap.read()

    img = cv2.flip(img ,1)

    #Detection of hand
    hands , img = detector.findHands(img, flipType=False , draw=False)

    # Draw all buttons
    cv2.rectangle(img,(800, 50),(800 + 400, 70 + 100), (200, 200, 200),
                  cv2.FILLED)
    cv2.rectangle(img, (800 , 50),(800 + 400, 70 + 100),
                  (100, 100, 100), 3)
    for button in buttonList:
        button.draw(img)

    #Check for hand
    if hands:
        lmList =hands[0]['lmList']
        length,_,img = detector.findDistance(lmList[8][:2],lmList[12][:2],img)
        # print(length)
        x,y = lmList[8][:2]
        if length < 50 :
            for i, button in enumerate(buttonList):
                if button.clickCheck(x,y,img) and delayCounter == 0:
                    myValue = button.value
                    if myValue == "=":
                        myEquation = str(eval(myEquation))
                    elif myValue == "C":
                        myEquation = ""
                    else:
                        myEquation += myValue

                    delayCounter=1
    #avoid duplicate
    if delayCounter != 0:
        delayCounter +=1
        if delayCounter >10 :
            delayCounter = 0
    #Display the result
    cv2.putText(img, myEquation, (800, 135), cv2.FONT_HERSHEY_DUPLEX,
                    3, (100, 100, 100), 3)

    # display image
    cv2.imshow("Image",img)
    key = cv2.waitKey(1)
    if key ==ord('c'):
        break
cap.release()
cv2.destroyAllWindows()