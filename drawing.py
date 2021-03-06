import numpy as np
import cv2

canvas = np.zeros((300,300,3), dtype='uint8')
green = (0, 255, 0)
cv2.line(canvas, (0,0), (300,300), green)
cv2.imshow("canvas", canvas)
cv2.waitKey(0)

red = (0, 0, 255)
cv2.line(canvas, (0, 300), (300, 0), red)
cv2.imshow('canvas', canvas)
cv2.waitKey(0)

centerX, centerY = (canvas.shape[1]//2, canvas.shape[0]//2)
white = (255, 255, 255)
for r in range(0, 175, 25):
    cv2.circle(canvas, (centerX, centerY), r, white)
cv2.imshow("canvas", canvas)
cv2.waitKey(0)