import numpy as np
import cv2

image = cv2.imread('/home/quan/Downloads/lam-lai-cmnd5.jpg')

blur = np.hstack([
    cv2.medianBlur(image, 7, 0),
    cv2.GaussianBlur(image, (7,7), 0),
    cv2.bilateralFilter(image,7,31 ,31)
])

cv2.imshow('Gaussian', blur)
cv2.waitKey(0)

