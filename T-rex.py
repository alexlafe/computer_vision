import cv2
from PIL import ImageGrab
import numpy as np
import time
import keyboard

def grabScreen(bbox=None):
    img = ImageGrab.grab(bbox=bbox)
    img = np.array(img)
    img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
    return img

while True:
    area = grabScreen(bbox=(540, 495, 1350, 660))

    zone = grabScreen(bbox=(655, 560, 740, 600))

    # 640, 550, 730, 610
    test = zone.mean()
    print(zone.shape)            
    print(test)

    if test != 247.0 and test > 38.41639215686274:
        keyboard.press("space")
        time.sleep(0.1)                                                                                                               
        keyboard.release("space")       

    cv2.imshow("Screen", area)

    if cv2.waitKey(1) == ord('q'):
        break
