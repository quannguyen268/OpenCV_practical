import cv2
import numpy as np




image = cv2.imread('/home/quan/Downloads/125300751_4791055530966209_467701909596726996_n.jpg')
M = np.ones(image.shape, dtype='uint8')*100
color = cv2.subtract(image, M)


one = np.zeros((image.shape[0], image.shape[1],3), dtype='uint8')
ones = [120,140,155]
lower = boundaries
upper = boundaries
lower = np.array(lower, dtype='uint8')
upper = np.array(upper, dtype='uint8')
mask = cv2.inRange(color, lower, upper)
output = cv2.bitwise_and(color, color, mask=mask)
cv2.imshow("mask", output)
cv2.waitKey(0)


gray = cv2.cvtColor(color, cv2.COLOR_BGR2GRAY)
thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)[1]
cv2.imshow("im", color)
cv2.waitKey(0)