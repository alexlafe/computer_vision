import numpy as np
import math
import matplotlib.pyplot as plt
from collections import defaultdict
from skimage.measure import regionprops, label

def count_lakes_and_bays(region): #функция для подсчёта озёр и заливов у символов
    symbol = ~region.image
    lb = label(symbol)
    regs = regionprops(lb)
    lakes = 0
    bays = 0
    for reg in regionprops(lb):
        flag = True
        for y, x in reg.coords:
            if y == 0 or x == 0 or y == region.image.shape[0] - 1 or x == region.image.shape[1] - 1:
                flag = False
                break
        lakes += int(flag)
        bays += int(not flag)
    return lakes, bays

def has_vertical_line(region): #функция для определния наличия вертикальной линии
    return 1. in region.image.mean(0)


def rec_symbols (im_region): #функция для опредления символов по кол-ву озёр и заливов
    result = defaultdict(lambda: 0)
    labeled = label(im_region)
    regions = regionprops(labeled)

    for region in regions:
        lakes, bays = count_lakes_and_bays(region)
        if lakes == 0:
            if np.all(region.image):
                result["-"] += 1
            elif has_vertical_line(region):
                result["1"] += 1
            elif bays == 2:
                result["/"] += 1
            elif math.floor(region.orientation * 10) == 15:
                result["W"] += 1
            elif region.eccentricity > 0.65:
                result["X"] += 1
            else:
                result["*"] += 1
        elif lakes == 1:
            if bays == 3:
                result["A"] += 1
            elif bays == 4:
                result["0"] += 1
            elif region.eccentricity > 0.65:
                result["P"] += 1
            else:
                result["D"] += 1
        elif lakes == 2:
            if has_vertical_line(region) and bays == 2:
                result["B"] += 1
            else:
                result["8"] += 1
        else: #считаем также символы не из алфавита
            result["unknown"] += 1
    return result

image = plt.imread("C:\\Users\Александр\Downloads\symbols.png")
image = np.mean(image, 2)
image[image > 0] = 1

labeled = label(image)
rec = rec_symbols(labeled)

for i in rec.keys():
    print(i, rec[i])

plt.imshow(image)
plt.show()