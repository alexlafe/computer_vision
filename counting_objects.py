import numpy as np
import matplotlib.pyplot as plt
from skimage.measure import label, regionprops
from skimage.morphology import binary_erosion, binary_dilation, binary_closing, binary_opening

#создаём 5 масок для всех типов фигур
mask_1 = np.array([[1, 1, 1, 1, 1, 1],
                   [1, 1, 1, 1, 1, 1],
                   [1, 1, 1, 1, 1, 1],
                   [1, 1, 1, 1, 1, 1]])

mask_2 = np.array([[1, 1, 1, 1, 1, 1],
                   [1, 1, 1, 1, 1, 1],
                   [1, 1, 0, 0, 1, 1],
                   [1, 1, 0, 0, 1, 1]])

mask_3 = np.array([[1, 1, 0, 0, 1, 1],
                   [1, 1, 0, 0, 1, 1],
                   [1, 1, 1, 1, 1, 1],
                   [1, 1, 1, 1, 1, 1]])

mask_4 = np.array([[1, 1, 1, 1],
                   [1, 1, 1, 1],
                   [1, 1, 0, 0],
                   [1, 1, 0, 0],
                   [1, 1, 1, 1],
                   [1, 1, 1, 1]])

mask_5 = np.array([[1, 1, 1, 1],
                   [1, 1, 1, 1],
                   [0, 0, 1, 1],
                   [0, 0, 1, 1],
                   [1, 1, 1, 1],
                   [1, 1, 1, 1]])

image = np.load("C:\\Users\Александр\Downloads\ps.npy.txt")
labeled = label(image)

count = np.max(labeled)
print('Total count of objects: ' + str(count))

#по отдельности применяем все маски и считаем кол-во объектов для каждой фигуры
fig1 = binary_erosion(labeled, mask_1)
c_fig1 = np.max(label(fig1))
print("Figure 1: " + str(c_fig1))

fig2 = binary_erosion(labeled, mask_2)
c_fig2 = np.max(label(fig2)) - c_fig1 #от фигур с дырками снизу и сверху необходимо отнимать кол-во фигур без дырок, тк эти маски их включают
print("Figure 2: " + str(c_fig2))

fig3 = binary_erosion(labeled, mask_3)
c_fig3 = np.max(label(fig3)) - c_fig1
print("Figure 3: " + str(c_fig3))

fig4 = binary_erosion(labeled, mask_4)
c_fig4 = np.max(label(fig4))
print("Figure 4: " + str(c_fig4))

fig5 = binary_erosion(labeled, mask_5)
c_fig5 = np.max(label(fig5))
print("Figure 5: " + str(c_fig5))

#проверка решения
if c_fig1 + c_fig2 + c_fig3 + c_fig4 + c_fig5 == count:
    print("The task was solved correctly")
else:
    print("The task was solved incorrectly")

plt.imshow(image)
plt.show()