import numpy as np
import cv2
import mahotas
im = cv2.imread('download.jpeg')
gray_im = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
blurred = cv2.pyrMeanShiftFiltering(im, 21,51)
gray = cv2.cvtColor(blurred, cv2.COLOR_BGR2GRAY)

cv2.imshow('download.jpeg', im)


# cv2.imshow('image', gray_im)
for i in range(0, gray_im.shape[0]):
    for j in range(0, gray_im.shape[1]):
        if gray_im[i,j] > 100:
            gray_im[i,j] = 255
        if gray_im[i,j] <= 100:
            gray_im[i,j] = 0


cv2.imshow('image', gray_im)
cv2.waitKey(0)

# (thresh1) = cv2.threshold(gray, 100, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]
# cv2.imshow('thresh binary', thresh1)
#
# (threshInv) = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)[1]
# cv2.imshow('thresh binary inverse', threshInv)
#
# cv2.imshow('Coins', cv2.bitwise_and(gray_im, gray_im, mask=thresh1))
#
# cv2.waitKey(0)
#
#
#
# T = mahotas.thresholding.rc(blurred)
# print('Riddle thresh: {}'.format(T))
# thresh = im.copy()
# thresh[thresh>T] = 255
# thresh[thresh<T] = 0
# # thresh = cv2.bitwise_not(thresh)
# cv2.imshow('riddle', thresh)
#
# canny = cv2.Canny(gray, 30, 150)
# cv2.imshow("Canny", canny)
# cv2.waitKey(0)
#
# (contour, _) = cv2.findContours(thresh1, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
#
# coins = im.copy()
# cv2.drawContours(coins, contour, -1, (0, 255, 0), 2)
# cv2.imshow('coins', coins)
# cv2.waitKey(0)