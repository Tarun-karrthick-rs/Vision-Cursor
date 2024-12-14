# Vision-Cursor 👀🖱️

Vision-Cursor is a project that allows users to control the mouse pointer using their eye movements. It uses OpenCV to detect faces and eyes through the webcam, and pyautogui to move the mouse cursor based on the detected eye positions. The program also simulates a mouse click when both eyes are detected. 👁️👁️

## Features 🌟

- **Eye Tracking**: Tracks the position of the eyes in real-time using OpenCV's Haar Cascade Classifiers. 🎯
- **Smooth Mouse Movement**: The movement of the mouse cursor is smoothed by averaging the eye position over time. 💨
- **Automatic Click**: Simulates a mouse click when both eyes are detected. 👆
- **Real-Time Display**: Displays the video feed with detected eyes marked by a green circle. 🎥

## Requirements 📋

- Python 3.x 🐍
- OpenCV 📸
- pyautogui 🖱️
- numpy ➗

## Installation ⚙️

1. Clone the repository or download the code files.
2. Install the necessary Python packages using the command:


   pip install -r requirements.txt

## Code Overview 💻

- **Face and Eye Detection**: Uses OpenCV’s Haar Cascade Classifiers to detect faces and eyes from the webcam feed. 👁️
- **Smooth Movement**: Smooths the mouse cursor movement by averaging the new eye position with the previous position, controlled by the `smooth_factor` variable. 🐾
- **Click Detection**: Detects when both eyes are visible in the frame and simulates a mouse click. 🖱️✅
- **Real-Time Webcam Feed**: Displays the webcam feed with green circles marking the detected eyes. 📹👁️

## Configuration ⚙️

- You can adjust the `smooth_factor` variable to control the speed and smoothness of the mouse movement. 🕹️
- The program uses your default webcam. 📷

To run the program, simply execute `eye_control.py`. The webcam feed will open, and the mouse will follow your eye movements. Press `q` to stop the program. 
