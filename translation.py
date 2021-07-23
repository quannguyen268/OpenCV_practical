import cv2
import numpy as np

image = cv2.imread('/home/quan/Downloads/4.png')
M1 = np.float32([[1,0,75], [0,1,25]])  # right 25, up 25
trans1 = cv2.warpAffine(image, M1, (image.shape[1], image.shape[0]))
cv2.imshow("image", trans1)
cv2.waitKey(0)

M2 = np.float32([[1, 0, -75], [0, 1, -25]])    # left 25, down 25
trans2 = cv2.warpAffine(image, M2, (image.shape[1], image.shape[0]))
cv2.imshow("image", trans2)
cv2.waitKey(0)