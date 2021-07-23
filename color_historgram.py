from __future__ import print_function
import matplotlib.pyplot as plt
import numpy as np
import cv2
import numpy as np

np.random.normal()


image1 = cv2.imread('/home/quan/Pictures/shiba1.jpg')
image1 = cv2.cvtColor(image1, cv2.COLOR_BGR2GRAY)
cv2.imshow('image1', image1)


image2 = cv2.imread('/home/quan/Pictures/shiba2.jpg')
image2 = cv2.cvtColor(image2, cv2.COLOR_BGR2GRAY)







def compute_hist(img):
    hist = np.zeros((256,))
    h, w = img.shape[:2]
    for i in range(h):
        for j in range(w):
            hist[img[i,j]] += 1

    return hist

def histogram_similarity(hist_1, hist_2):
    x = [(i - j) * (i - j) for (i, j) in zip(hist_1,hist_2)]

    similarity = np.sqrt(np.sum(x))
    return similarity

def histogram_distance(hist_1, hist_2):
    minima = np.minimum(hist_1, hist_2)
    distance = np.true_divide(np.sum(minima), np.sum(hist_2))

    return distance

hist1 = compute_hist(image1)
hist2 = compute_hist(image2)

print(hist1, hist2)
# print(histogram_similarity(hist2,hist1))




# for (chan, color) in zip(chans, colors):
#     hist = cv2.calcHist([chan], [0], None, [256], [0,256])
#     plt.plot(hist, color=color)
#     plt.xlim([0,256])


#
# fig = plt.figure()
#
# ax = fig.add_subplot(131)
# hist = cv2.calcHist([chans[1], chans[0]], [0,1], None, [32, 32], [0, 256, 0, 256])
# p = ax.imshow(hist, interpolation='nearest')
# ax.set_title('2D Color Histogram for G and B')
# plt.colorbar(p)
#
# ax = fig.add_subplot(132)
# hist = cv2.calcHist([chans[1], chans[2]], [0, 1], None,
# [32, 32], [0, 256, 0, 256])
# p = ax.imshow(hist, interpolation = "nearest")
# ax.set_title("2D Color Histogram for G and R")
# plt.colorbar(p)
#
# ax = fig.add_subplot(133)
# hist = cv2.calcHist([chans[0], chans[2]], [0, 1], None,
# [32, 32], [0, 256, 0, 256])
# p = ax.imshow(hist, interpolation = "nearest")
# ax.set_title("2D Color Histogram for B and R")
# plt.colorbar(p)
# plt.show()