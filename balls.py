import cv2
import numpy as np

cv2.namedWindow("Image", cv2.WINDOW_AUTOSIZE)

cam = cv2.VideoCapture(0)
cam.set(cv2.CAP_PROP_AUTO_WB, 0)

position = [0, 0]

def on_mouse_click(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        global position
        position = [y, x]

cv2.setMouseCallback("Image", on_mouse_click)

while cam.isOpened:
    _, frame = cam.read()
    frame = cv2.GaussianBlur(frame, (21, 21), 0)

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    pixel = hsv[position[0], position[1]]
    cv2.putText(frame, f"HSV = {pixel}", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 0))

    cv2.circle(frame, position[::-1], 5, (255, 255, 255), 2)
    cv2.imshow("Image", frame)
    key = cv2.waitKey(50)
   
    if key == ord('q'):
        break
cv2.destroyAllWindows()