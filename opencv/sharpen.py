import cv2
import numpy as np
import matplotlib.pyplot as plt

def sharpen():
    return (([1,1,1],[1,1,1],[1,1,1]))

def filtering(image, kernel):
    m,n = kernel.shape()
    if m==n:
        y,x = image.shape[:2]
        new_image = np.zeroes((y,x))
        for i in range(y):
            for j in range(x):
                new_image[i][j] = np.sum(image[i:i+m, j:j+m]*kernel)
        return new_image
    
img = cv2.imread("x")
img_array = np.array(img)

plt.figure(figsize=(10, 5))
plt.subplot(1,2,1)
plt.imshow(img, cmap='grey')
plt.subplot(1,2,2)
plt.imshow(filtering(img_array, sharpen()), cmap='grey')
