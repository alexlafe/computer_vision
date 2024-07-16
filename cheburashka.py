import cv2
import matplotlib.pyplot as plt
import numpy as np
from skimage.morphology import binary_dilation, binary_erosion

chebu = cv2.imread("C:\\1\\cheburashka.jpg")
news = cv2.imread("C:\\1\\news.jpg")
rows, cols, _ = chebu.shape

pts_chebu = np.float32([[0, 0], [0, rows], [cols, 0], [cols, rows]])
pts_news = np.float32([[18, 24], [41, 295], [430, 54], [434, 267]])

M = cv2.getPerspectiveTransform(pts_chebu, pts_news)
aff = cv2.warpPerspective(chebu, M, (news.shape[1], news.shape[0]))

pos = np.where(aff == np.array([0, 0, 0]))
result = news.copy()
result[pos] = 0

plt.figure()
plt.imshow(result)
plt.show()