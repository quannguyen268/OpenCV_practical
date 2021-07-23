import numpy as np
import cv2
import PIL.Image as Image

image = cv2.imread('/home/quan/Downloads/4.png')
(h ,w) = image.shape[:2]
center = (w//2, h//2)
print(image[0,0])

import io

img = Image.open('/home/quan/Downloads/4.png', mode='r')


img_byte_arr = io.BytesIO()
img.save(img_byte_arr, format='PNG')
img_byte_arr = img_byte_arr.getvalue()

M = cv2.getRotationMatrix2D(center, 180, 1.0)
rotate = cv2.warpAffine(image, M, (w,h))
# cv2.imshow("rotate", rotate)
# cv2.waitKey(0)

scale = 1000
dim = (scale, int(scale*(h/w)))
resized = cv2.resize(image, dim, interpolation=cv2.INTER_AREA)
# cv2.imshow("im", resized)
# cv2.waitKey(0)