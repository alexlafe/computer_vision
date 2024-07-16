from skimage.measure import label, regionprops
from skimage.morphology import binary_closing
import cv2

pencils = 0

for n in range(1, 13):
    image = cv2.imread(f"C:\\1\\img ({n}).jpg")
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    gray[gray > 125] = 0
    gray[gray != 0] = 255
    gray = binary_closing(binary_closing(gray))
    labeled = label(gray)
    regions = regionprops(labeled)
    figures = []

    for i in range(len(regions)):
        area = regions[i].image.shape[0] * regions[i].image.shape[1]
        if area > 10000:
            figures.append(regions[i])
    k = 0

    for img in figures:
        if round(img.eccentricity, 3) >= 0.998 and img.area > 250000:
            k += 1

    pencils += k
    print(f"Изобаржение {n}: кол-во - {k}")

print(f"Общее кол-во карандашей - {pencils}")
