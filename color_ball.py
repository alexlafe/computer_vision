import cv2
import numpy as np

cv2.namedWindow("Image", cv2.WINDOW_AUTOSIZE)

cam = cv2.VideoCapture(0)
cam.set(cv2.CAP_PROP_AUTO_WB, 0)

#red
lower_r = np.array([160, 145, 135])
upper_r = np.array([190, 255, 255])

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

    mask_r = cv2.inRange(hsv, lower_r, upper_r)
    mask_o = cv2.inRange(hsv, lower_o, upper_o)
    mask_y = cv2.inRange(hsv, lower_y, upper_y)

    contours_r, _ = cv2.findContours(mask_r, cv2.RETR_EXTERNAL, cv2. CHAIN_APPROX_SIMPLE)
    contours_o, _ = cv2.findContours(mask_o, cv2.RETR_EXTERNAL, cv2. CHAIN_APPROX_SIMPLE)
    contours_y, _ = cv2.findContours(mask_y, cv2.RETR_EXTERNAL, cv2. CHAIN_APPROX_SIMPLE)

    if len(contours_r) > 0:
        cv2.putText(frame, f"color = red", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 0))
        c = max(contours_r, key=cv2.contourArea)
        (x, y), radius = cv2.minEnclosingCircle(c)
        if radius > 20: #значение 20, чтобы убрать шум
            cv2.circle(frame, (int(x), int(y)), int(radius), (0, 255, 255), 0)

    if len(contours_o) > 0:
        cv2.putText(frame, f"color = orange", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 0))
        c = max(contours_o, key=cv2.contourArea)
        (x, y), radius = cv2.minEnclosingCircle(c)
        if radius > 20: #значение 20, чтобы убрать шум
            cv2.circle(frame, (int(x), int(y)), int(radius), (0, 255, 255), 0)

    if len(contours_y) > 0:
        cv2.putText(frame, f"color = yellow", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 0))
        c = max(contours_y, key=cv2.contourArea)
        (x, y), radius = cv2.minEnclosingCircle(c)
        if radius > 20: #значение 20, чтобы убрать шум
            cv2.circle(frame, (int(x), int(y)), int(radius), (0, 255, 255), 0)
    
    cv2.imshow("Image", frame)
    key = cv2.waitKey(50)
   
    if key == ord('q'):
        break
cv2.destroyAllWindows()