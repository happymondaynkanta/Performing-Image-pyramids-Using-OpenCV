# subsampling & upsampling --- Laplacian Pyramid
import cv2
import numpy as np
from matplotlib import pyplot as plt


img = cv2.imread("lena.jpg")
layer = img.copy()
gp = [layer]


for i in range(6): # reduce image 5 times
    layer = cv2.pyrDown(layer)
    gp.append(layer)


layer = gp[5]
cv2.imshow('Upper Level Gaussian Pyramid', layer)
lp = [layer]


for i in range(5, 0, -1):
    gaussian_entended = cv2.pyrUp(gp[i])
    laplacian = cv2.subtract(gp[i-1], gaussian_entended)
    cv2.imshow(str(i), laplacian)


cv2.imshow("Original Image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
