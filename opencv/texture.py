import cv2
import numpy as np

img = cv2.imread("x")
grey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

edges = cv2.Canny(grey, 100, 200)
kernel = np.ones((5,5), np.float32)/25
texture = cv2.filter2D(grey, -1, kernel)
