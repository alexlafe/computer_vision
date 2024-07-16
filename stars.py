from email.mime import image
import numpy as np
import matplotlib.pyplot as plt
from scipy.misc import face
from skimage.measure import label
from skimage.morphology import binary_erosion, binary_dilation, binary_closing, binary_opening

mask_1 = np.array([[0, 0, 1, 0, 0],
                   [0, 0, 1, 0, 0],
                   [1, 1, 1, 1, 1],
                   [0, 0, 1, 0, 0],
                   [0, 0, 1, 0, 0],])

mask_2 = np.array([[1, 0, 0, 0, 1],
                   [0, 1, 0, 1, 0],
                   [0, 0, 1, 0, 0],
                   [0, 1, 0, 1, 0],
                   [1, 0, 0, 0, 1],])

image = np.load("C:\\Users\Александр\Downloads\stars.npy")
labeled = label(image)

val1 = binary_erosion(labeled, mask_1)
pl = np.max(label(val1))
print("Pluses: " + str(pl))

val2 = binary_erosion(labeled, mask_2)
st = np.max(label(val2))
print("Crosses: " + str(st))

plt.subplot(121)
plt.imshow(labeled)
plt.subplot(122)
plt.imshow(val2)
plt.show()
