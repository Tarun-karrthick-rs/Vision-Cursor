
import cv2
import pyautogui
import numpy as np

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml')


cam = cv2.VideoCapture(0)


screen_w, screen_h = pyautogui.size()


prev_x, prev_y = 0, 0
smooth_factor = 5 #set higher for more smoother

click_detected = False

while True:
    ret, frame = cam.read()
    if not ret:
        print("Failed to grab frame")
        break
    

    frame = cv2.flip(frame, 1)

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)
    if len(faces) == 0:
        print("No faces detected")

    for (x, y, w, h) in faces:
        face_roi = frame[y:y + h, x:x + w]
        eyes = eye_cascade.detectMultiScale(face_roi)

        if len(eyes) == 0:
            print("No eyes detected in face region")
        
        if len(eyes) > 0:
            for (ex, ey, ew, eh) in eyes:
                eye_center_x = x + ex + ew // 2
                eye_center_y = y + ey + eh // 2

                screen_x = screen_w * (eye_center_x / frame.shape[1])
                screen_y = screen_h * (eye_center_y / frame.shape[0])
                screen_x = prev_x + (screen_x - prev_x) / smooth_factor
                screen_y = prev_y + (screen_y - prev_y) / smooth_factor

                pyautogui.moveTo(screen_x, screen_y)

                prev_x, prev_y = screen_x, screen_y

                cv2.circle(frame, (eye_center_x, eye_center_y), 3, (0, 255, 0), -1)

            if len(eyes) == 2 and not click_detected:
                print("Both eyes detected, clicking")
                pyautogui.click()
                click_detected = True

    if len(eyes) == 0:
        click_detected = False

    cv2.imshow('Eye Controlled Mouse', frame)


    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cam.release()
cv2.destroyAllWindows()

