import numpy as np
import matplotlib.pyplot as plt
from skimage.measure import label
from skimage.morphology import binary_erosion, binary_dilation, binary_opening


image = np.load("C:\\Users\Александр\Downloads\wires6.npy.txt")
labeled = label(image)

mask = np.array([[0, 1, 0],
                 [0, 1, 0],
                 [0, 1, 0]])

count_wires = np.max(labeled) #кол-во проводов

for i in range(1, count_wires + 1):
    one_wire = np.zeros_like(labeled)
    one_wire[labeled == i] = 1
    holes = binary_opening(one_wire, mask) #делаем дырки
    this_labeled = label(holes)
    count_wires = np.max(this_labeled)
    if count_wires > 1:
        print(str(i) + " wire is torn into " + str(count_wires) + " pieces")
    else:
        print(str(i) + " wire isn't torn")

plt.imshow(image)
plt.show()