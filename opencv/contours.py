import cv2
import numpy as np
img = cv2.imread("rabbit.png")
grey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
_, binary_img = cv2.threshold(grey, 127, 255, cv2.THRESH_BINARY)

contours, _ = cv2.findContours(binary_img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

cv2.drawContours(img, contours, -1, (0,255,0), 3)

cv2.imshow('contours', img)
