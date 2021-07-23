from matplotlib import pyplot as plt
import cv2

image = cv2.imread('/home/quan/Downloads/lam-lai-cmnd5.jpg')
image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow('Original image', image)

hist = cv2.calcHist([image], [0], None, [256], [0, 256])

plt.figure()
plt.title('Grayscale Histogram')
plt.xlabel('Bins')
plt.ylabel("# of Pixels")
plt.plot(hist)
plt.xlim([0,256])
plt.show()
cv2.waitKey(0)

