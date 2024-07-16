import cv2
import numpy as np
import random

cv2.namedWindow("Image", cv2.WINDOW_AUTOSIZE)

cam = cv2.VideoCapture(0)
cam.set(cv2.CAP_PROP_AUTO_WB, 0)

color = ["Yellow", "Blue", "Orange"] 

#blue
lower_b = np.array([95, 150, 120])
upper_b = np.array([105, 255, 255])

#orange
lower_o = np.array([0, 130, 190])
upper_o = np.array([25, 255, 255])

#yellow
lower_y = np.array([10, 150, 145])
upper_y = np.array([45, 255, 255])

while cam.isOpened:
    _, frame = cam.read()
    frame = cv2.GaussianBlur(frame, (21, 21), 0)
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    mask_b = cv2.inRange(hsv, lower_b, upper_b)
    mask_o = cv2.inRange(hsv, lower_o, upper_o)
    mask_y = cv2.inRange(hsv, lower_y, upper_y)

    contours_b, _ = cv2.findContours(mask_b, cv2.RETR_EXTERNAL, cv2. CHAIN_APPROX_SIMPLE)
    contours_o, _ = cv2.findContours(mask_o, cv2.RETR_EXTERNAL, cv2. CHAIN_APPROX_SIMPLE)
    contours_y, _ = cv2.findContours(mask_y, cv2.RETR_EXTERNAL, cv2. CHAIN_APPROX_SIMPLE)

    color_balls = {}

    if len(contours_b) > 0:
        c_b = max(contours_b, key=cv2.contourArea)
        (x_b, y_b), radius_b = cv2.minEnclosingCircle(c_b)
        color_balls[x_b] = "Blue"
        if radius_b > 20: #значение 20, чтобы убрать шум
            cv2.circle(frame, (int(x_b), int(y_b)), int(radius_b), (0, 255, 255), 0)

    if len(contours_o) > 0:
        c_o = max(contours_o, key=cv2.contourArea)
        (x_o, y_o), radius_o = cv2.minEnclosingCircle(c_o)
        color_balls[x_o] = "Orange"
        if radius_o > 20: #значение 20, чтобы убрать шум
            cv2.circle(frame, (int(x_o), int(y_o)), int(radius_o), (0, 255, 255), 0)

    if len(contours_y) > 0:
        c_y = max(contours_y, key=cv2.contourArea)
        (x_y, y_y), radius_y = cv2.minEnclosingCircle(c_y)
        color_balls[x_y] = "Yellow"
        if radius_y > 20: #значение 20, чтобы убрать шум
            cv2.circle(frame, (int(x_y), int(y_y)), int(radius_y), (0, 255, 255), 0)

    color_balls = {k : color_balls[k] for k in sorted(color_balls)}
    
    key = cv2.waitKey(50)
   
    if key == ord('q'):
        break
    if key == ord('p'):
        for key in color_balls:
            new_list_balls.append(color_balls[key])
        print(new_list_balls)
        cv2.putText(frame, f"{new_list_balls}", (10, 50), cv2.FONT_HERSHEY_COMPLEX, 0.7, (255, 255, 0))
        if color == new_list_balls:
            cv2.putText(frame, "True", (10, 70), cv2.FONT_HERSHEY_COMPLEX, 0.7, (255, 255, 0))
        else:
            cv2.putText(frame, "False", (10, 70), cv2.FONT_HERSHEY_COMPLEX, 0.7, (255, 255, 0))

    if key == ord('b'):
        random.shuffle(color)
        print(color)
    cv2.putText(frame, f"{color}", (10, 30), cv2.FONT_HERSHEY_COMPLEX, 0.7, (255, 255, 0))

    new_list_balls = []

    cv2.imshow("Image", frame)

cv2.destroyAllWindows()