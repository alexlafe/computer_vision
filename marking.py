import matplotlib.pyplot as plt
import numpy as np

def check(B, y, x):
    if not 0 <= x < B.shape[0]:
        return False
    if not 0 <= y < B.shape[1]:
        return False
    if B[y, x] != 0:
        return True
    return False

def neighbors2(B, y, x):
    left = y, x-1
    top = y - 1, x
    if not check(B, *left):
        left = None
    if not check(B, *top):
        top = None
    return left, top

def exists(neighbors):
    return not all([n is None for n in neighbors])

def find(label, linked):
    j = label
    while linked[j] != 0:
        j = linked[j]
    return j

def union(label1, label2, linked):
    j = find(label1, linked)
    k = find(label2, linked)
    if j != k:
        linked[k] = j


def two_pass_labeling(B):
    B = (B.copy() * - 1).astype("int")
    linked = np.zeros(len(B), dtype="uint")
    labels = np.zeros_like(B)
    label = 1
    for row in range(B.shape[0]):
        for col in range(B.shape[1]):
            if B[row, col] != 0:
                n = neighbors2(B, row, col)
                if not exists(n):
                    m = label
                    label += 1
                else:
                    lbs = [labels[i] for i in n if i is not None]
                    m = min(lbs)
                labels[row, col] = m
                for i in n:
                    if i is not None:
                        lb = labels[i]
                        if lb != m:
                            union(m, lb, linked)
    for row in range(B.shape[0]):
        for col in range(B.shape[1]):
            if B[row, col] != 0:
                new_label = find(labels[row, col], linked)
                if new_label != labels[row, col]:
                    labels[row, col] = new_label

    uniq = np.unique(labels)
    d = {i: l for (i, l) in enumerate(uniq)}
    for y in range(labels.shape[0]):
        for x in range(labels.shape[1]):
            for m, n in d.items():
                if labels[y, x] != 0 and labels[y, x] == n:
                    labels[y, x] = m

    return labels

if __name__ == "__main__":
    image = np.zeros((20, 20), dtype='int32')
    
    image[1:-1, -2] = 1
    
    image[1, 1:5] = 1
    image[1, 7:12] = 1
    image[2, 1:3] = 1
    image[2, 6:8] = 1
    image[3:4, 1:7] = 1
    
    image[7:11, 11] = 1
    image[7:11, 14] = 1
    image[10:15, 10:15] = 1
    
    image[5:10, 5] = 1
    image[5:10, 6] = 1

    labeled_image = two_pass_labeling(image)
    
    plt.figure(figsize=(12, 5))
    plt.subplot(121)
    plt.imshow(image)
    plt.subplot(122)
    plt.imshow(labeled_image.astype("uint8"))
    plt.show()