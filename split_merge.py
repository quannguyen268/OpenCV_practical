import numpy as np
import cv2
import matplotlib.pyplot as plt



# Read an image
origin_bgr = cv2.imread('/home/quan/PycharmProjects/OpenCV_practical/157737215_250521136748497_390207163245905894_o.jpeg', 1)
img_bgr = cv2.cvtColor(origin_bgr, cv2.COLOR_BGR2GRAY )

# Histogram plotting of the image




# get height and width of the image
height, width = img_bgr.shape

# for i in range(0, height - 1):
#     for j in range(0, width - 1):
#         # Get the pixel value
#         pixel = img_bgr[i, j]
#
#         # Negate each channel by
#         # subtracting it from 255
#
#         # 1st index contains red pixel
#         pixel = 255 - pixel
#
#
#
#         # Store new values in the pixel
#         img_bgr[i, j] = pixel
#
#     # Display the negative transformed image
# cv2.imshow('img', img_bgr)
# cv2.waitKey(0)

# Histogram plotting of the
# negative transformed image

gray = np.zeros(origin_bgr.shape[:2], dtype='uint8' )
(B,G,R) = cv2.split(origin_bgr)

for i in range(0, origin_bgr.shape[0]):
    for j in range(0, origin_bgr.shape[1]):
        gray[i,j] = 0.2989 * R[i,j] + 0.5870 * G[i,j] + 0.1140 * B[i,j]



cv2.imshow('gray', gray)
cv2.imshow('R', R)
cv2.imshow('G', G)
cv2.imshow('B', B)

merge = cv2.merge([B,G,R])
cv2.imshow('Merge', merge)
cv2.waitKey(0)

zeros = np.zeros(origin_bgr.shape[:2], dtype = "uint8")
cv2.imshow("Red", cv2.merge([zeros, zeros, R]))
cv2.imshow("Green", cv2.merge([zeros, G, zeros]))
cv2.imshow("Blue", cv2.merge([B, zeros, zeros]))
cv2.waitKey(0)