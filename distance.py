from __future__ import print_function
import matplotlib.pyplot as plt
import cv2
import numpy as np

np.random.normal()


image1 = cv2.imread('/home/quan/Pictures/shiba1.jpg')
image1 = cv2.cvtColor(image1, cv2.COLOR_BGR2GRAY)
cv2.imshow('image1', image1)


image2 = cv2.imread('/home/quan/Pictures/shiba2.jpg')
image2 = cv2.cvtColor(image2, cv2.COLOR_BGR2GRAY)
cv2.imshow('image2', image2)        
cv2.waitKey(0)
cv2.destroyAllWindows()






def compute_hist(img):
    hist = np.zeros((256,1), dtype='uint8')
    h, w = img.shape[:2]
    for i in range(h):
        for j in range(w):
            hist[img[i,j]] += 1

    return hist

def histogram_similarity(hist_1, hist_2):
    x = [((i - j)**2)/(i+0.1) for (i, j) in zip(hist_1,hist_2)]
    similarity = np.sqrt(np.sum(x))
    return similarity



hist1 = compute_hist(image1)
hist2 = compute_hist(image2)


print("Histogram similarity: ",histogram_similarity(hist2,hist1))