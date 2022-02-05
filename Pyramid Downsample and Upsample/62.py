# subsampling & upsampling -- Gaussian Pyramid


import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread("lena.jpg")

lr1 = cv2.pyrDown(img)  # resize into half of original
lr2 = cv2.pyrDown(lr1)


cv2.imshow('Ori_image', img)
cv2.imshow('pyrDown1', lr1)
cv2.imshow('pyrDown2', lr2)



cv2.waitKey(0)
cv2.destroyAllWindows()
