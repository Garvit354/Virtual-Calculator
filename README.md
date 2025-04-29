# Virtual Hand Gesture Calculator

This project is a **Virtual Calculator** that uses **hand gestures** to interact with the calculator. In this no mouse or keyboard is needed! It uses your **webcam**, detects your hand using **MediaPipe (via cvzone)**, and allows you to press calculator buttons with just your fingers.

---

## Video Demo of the project 

![CalculationVideo](video/virtualCalculatorV.gif)


---

##  Features

- Allows finger-based button pressing
- Real-time feedback on screen
- Fully functional calculator (`+, -, *, /, %, (), C, =, .`)
- Built with **OpenCV**, **cvzone**, and **MediaPipe**

---

## ️ Tech Stack

- **Python**
- **OpenCV**
- **cvzone**
- **MediaPipe** (via `cvzone.HandTrackingModule`)

---

## How It Works

- Your webcam captures live video.
- The program detects your **index and middle fingers**.
- When your index and middle fingers touch (distance < threshold), it's treated as a "click".
- If your fingertip is over a button, it's considered pressed.
- The result or ongoing equation is shown at the top of the screen.

---

## Requirements
Python version
```bash
Python 3.7.6

```
Install dependencies using pip:

```bash
pip install opencv-python cvzone
pip install mediapipe==0.8.9
pip install cvzone==1.5.3
```
To Run this project 
```bash
python main.py
```

