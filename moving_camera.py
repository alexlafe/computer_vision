import cv2
import numpy as np

logo = cv2.imread("C:\\1\\cvlogo.png", cv2.IMREAD_UNCHANGED)
logo = cv2.resize(logo, (logo.shape[0] // 4, logo.shape[1] // 4)) #уменьшаем в 4 раза изображение
mask = logo[:, :, -1]
logo = logo[:, :, :-1]

# cv2.namedWindow("Image", cv2.WINDOW_AUTOSIZE)
# cv2.imshow("Image", image)
# key = cv2.waitKey(0)
# cv2.destroyAllWindows()

cv2.namedWindow("Image", cv2.WINDOW_AUTOSIZE)
cv2.namedWindow("Diff", cv2.WINDOW_AUTOSIZE)

cam = cv2.VideoCapture(0) 

background = None

while cam.isOpened:
    _, frame = cam.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray = cv2.GaussianBlur(gray, (21, 21), 0)

    if background is not None:
        diff = cv2.absdiff(gray, background)
        thresh = cv2.threshold(diff, 25, 255, cv2.THRESH_BINARY)[1]
        thresh = cv2.dilate(thresh, None, iterations=2)

        contours = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[0]

        for c in contours:
            area = cv2.contourArea(c)
            if area > 1000:
                x, y, w, h = cv2.boundingRect(c)
                cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

        cv2.imshow("Diff", thresh)

    cv2.imshow("Image", frame)
    key = cv2.waitKey(50)
    if key == ord('q'):
        break
    if key == ord('b'):
        background = gray.copy()
cv2.destroyAllWindows()