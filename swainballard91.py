from __future__ import print_function
# import matplotlib.pyplot as plt
import cv2
# copyright by nguyen van quan-20172769
import numpy as np
import os

folder = '/home/quan/Desktop/ggg/swainballard91/'
images = os.listdir('/home/quan/Desktop/ggg/swainballard91')

# compute histogram of each image
def compute_hist(img):
    hist = np.zeros((256,1))
    h, w = img.shape[:2]
    for i in range(h):
        for j in range(w):
            hist[img[i,j]] += 1

    return hist

# distance in swainballard91 report
def histogram_distance(hist_1, hist_2):
    minima = np.minimum(hist_1, hist_2)
    distance = np.true_divide(np.sum(minima), np.sum(hist_2))
    return distance


comp_origin = cv2.imread(folder+images[0])

comp_image = cv2.cvtColor(comp_origin, cv2.COLOR_BGR2GRAY)
comp_hist = compute_hist(comp_image)


origin1 = cv2.imread(folder+images[1])

imag1 = cv2.cvtColor(origin1, cv2.COLOR_BGR2GRAY)
hist1 = compute_hist(imag1)

origin2 = cv2.imread(folder+images[2])
imag2 = cv2.cvtColor(origin2, cv2.COLOR_BGR2GRAY)
hist2 = compute_hist(imag2)

origin3 = cv2.imread(folder+images[3])
imag3 = cv2.cvtColor(origin3, cv2.COLOR_BGR2GRAY)
hist3 = compute_hist(imag3)

d = []

list_image = {0: origin1,
              1: origin2,
              2: origin3}


list_dist = {0: [],
             1: [],
             2: []}

for (i,hist) in enumerate(zip((hist1, hist2, hist3))):
    d_i = histogram_distance(comp_hist, hist)
    list_dist[i].append(d_i)
    d.append(d_i)

d = sorted(d, reverse=True)





cv2.imshow('compare image', comp_origin)
for i in d :
    for j in range(0,3):
        if i == list_dist[j]:
            cv2.imshow('Accuracy : '+ str(i), list_image[j])
    cv2.waitKey(0)












