import numpy as np
import matplotlib.pyplot as plt
from skimage import color
from skimage.measure import label, regionprops

image = plt.imread("C:\\1\\balls_and_rects.png")
image = color.rgb2hsv(image)[:, :, 0]
uniq = np.unique(image) * 10
image = np.ceil(image * 10)
color = np.unique(np.ceil(uniq))
circle = {}
rectangle = {}
i = 0

for cl in color:
    circle["color" + str(i)] = 0
    rectangle["color" + str(i)] = 0
    img = image.copy()
    img[img != cl] = 0
    labeled = label(img)
    reg = regionprops(labeled)

    for r in reg:
        if np.all(r.image):
            circle["color" + str(i)] += 1
        else:
            rectangle["color" + str(i)] += 1
    i += 1

print("Circles = ", circle)
print("Rectangles = ", rectangle)
print("General count = ", np.sum(list(rectangle.values())) + np.sum(list(circle.values())))