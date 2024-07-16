import numpy as np
import matplotlib.pyplot as plt
import cv2
from skimage import color
from skimage.measure import label, regionprops
from skimage.morphology import binary_erosion, binary_dilation, binary_closing, binary_opening
from skimage.filters import threshold_otsu, sobel

im = plt.imread("C:\\Users\Александр\Downloads\\balls.png")
hsv = color.rgb2hsv(im)
binary = hsv[:, :, 0].copy()
binary[binary > 0] = 1
labeled = label(binary)
regions = regionprops(labeled)

colors = []
for reg in regions:
    cy, cx = reg.centroid
    colors.append(hsv[int(cy), int(cx), 0])

groups = [[],]
colors = sorted(colors)
delta = np.max(np.diff(colors)) / 2
for i in range(len(colors)):
    previous = colors[i-1]
    current = colors[i]
    if current - previous > delta:
        groups.append([])
    groups[-1].append(current)
print(len(groups))

result_colors = []
result_count = []
for grp in groups:
    result_count.append(len(grp))
    result_colors.append(np.mean(grp))
print(result_colors)
print(result_count)

plt.plot(np.diff(colors))
plt.show()

# print(cv2.getBuildInformation())

# cam = cv2.VideoCapture(0)
# if cam.isOpened():
#     ret, frame = cam.read()
#     print(frame.shape)
# cam.release()