#program to perform rotation, scaling and zooming on an image

import cv2
import numpy as np

def translate_image(img, dx, dy):
    rows, cols = img.shape[:2]
    translation_matrix = np.float32([[1,0,dx], [0,1,dy]])
    translated_image = cv2.warpAffine(src = img, M = translation_matrix, dsize=(cols, rows))
    return translated_image

img = cv2.imread("atsu.png")
height, width = img.shape[:2]

center = (width//2, height//2)

rotation_value = int(input("Enter degrees: "))
scaling_value = int(input("Enter zooming factor: "))

rotated = cv2.getRotationMatrix2D(center = center, angle = rotation_value, scale=1)
rotated_image = cv2.warpAffine(src = img, M = rotated, dsize=(width, height))

scaled = cv2.getRotationMatrix2D(center = center, angle = 0, scale=scaling_value)
scaled_image = cv2.warpAffine(src = img, M = scaled, dsize=(width, height))

h = int(input("Horizontal: "))
v = int(input("Vertical: "))

translated_image = translate_image(img = scaled_image, dx=h, dy=v)

cv2.imshow("Rotated", rotated_image)
cv2.imshow("Translated", translated_image)
