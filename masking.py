import numpy as np
import cv2



image = cv2.imread("/home/quan/Downloads/4.png")
cv2.imshow('image', image)

mask = np.zeros(image.shape[:2], dtype='uint8')
(cX, cY) = (image.shape[1] // 2, image.shape[0] // 2)
cv2.rectangle(mask, (cX - 150, cY - 150), (cX + 150, cY + 150), 255, -1)
cv2.imshow("Mask", mask)

masked = cv2.bitwise_and(image, image, mask= mask)
cv2.imshow("masked", masked)



cv2.circle(mask, (cX, cY), 500, 255, -1)
masked = cv2.bitwise_and(image, image, mask=mask)
cv2.imshow("masked", masked)
cv2.waitKey(0)


