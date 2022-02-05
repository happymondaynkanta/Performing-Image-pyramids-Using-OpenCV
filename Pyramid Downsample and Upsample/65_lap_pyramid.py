# subsampling & upsampling (using loop) ---  Laplacian & Gaussian Pyramid
# Laplacian Pyramid -- diff bet gaussian pyramind and it upper level pyramid

import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread("lena.jpg")

lp = cv2.pyrDown(img)
up = cv2.pyrUp(lp)
gaus_py = cv2.subtract(img, up)


cv2.imshow('Ori_image', img)
cv2.imshow('Lower_Pyramid', lp)
cv2.imshow('Upper_Pyramid', up)
cv2.imshow('Gaussian_Pyramid', gaus_py)

cv2.waitKey(0)
cv2.destroyAllWindows()
