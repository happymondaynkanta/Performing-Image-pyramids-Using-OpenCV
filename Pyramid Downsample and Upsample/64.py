# subsampling & upsampling (using loop) ---  Gaussian Pyramid
import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread("lena.jpg")
cv2.imshow('Ori_image', img)

layer = img.copy() # make copy of images

gp = [layer]

for i in range(6): # reduce image 5 times
    layer = cv2.pyrDown(layer)
    gp.append(layer)

    cv2.imshow(str(i), layer)


cv2.waitKey(0)
cv2.destroyAllWindows()
