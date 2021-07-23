import numpy as np
import cv2

a = np.zeros((300, 300), dtype='uint8')
rectangle = cv2.rectangle(a, (25, 25), (275, 275), 0, -1)
cv2.imshow("rectangle", rectangle)
print(a.shape)
b = np.ones((300, 300), dtype='uint8')
circle = cv2.circle(b, (150, 150), 150, 0, -1)
cv2.imshow("circle", circle)
cv2.waitKey(0)

bitwiseAnd = cv2.bitwise_and(rectangle, circle)
cv2.imshow("And", bitwiseAnd)

bitwiseOr = cv2.bitwise_or(rectangle, circle)
cv2.imshow("Or", bitwiseOr)

bitwiseXor = cv2.bitwise_xor(rectangle, circle)
cv2.imshow("Xor", bitwiseXor)

bitwiseNot = cv2.bitwise_not(circle)
cv2.imshow("Not", bitwiseNot)
cv2.waitKey(0)