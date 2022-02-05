# reconstruction blending using pyramid ---
# step 1: load the 2 images
# step 2: find the gaussian pyramid for both images
# step 3: from the gaussian pyramid, find their laplacian pyramids
# step 4: join each halves of both laplacian pyramids
# step 5: reconstruct the image from the merged pyramids

import cv2
import numpy as np

apple = cv2.imread("apple.jpg")
orange = cv2.imread("orange.jpg")

apple_orange = np.hstack((apple[:, :256], orange[:, 256:]))


# generate gaus pyramid for apple
gaus_apple1 = cv2.pyrDown(apple)
gaus_apple2 = cv2.pyrDown(gaus_apple1)

# generate gaus pyramid for orange
gaus_orange1 = cv2.pyrDown(orange)
gaus_orange2 = cv2.pyrDown(gaus_orange1)

# generate laplacian pyramid for apple
lp_apple2 = cv2.pyrUp(gaus_apple2)
lp_apple1 = cv2.pyrUp(gaus_apple1)

lap_apple2 = cv2.subtract(gaus_apple1, lp_apple2)
lap_apple1 = cv2.subtract(apple, lp_apple1)



# generate laplacian pyramid for orange
lp_orange2 = cv2.pyrUp(gaus_orange2)
lp_orange1 = cv2.pyrUp(gaus_orange1)

lap_orange2 = cv2.subtract(gaus_orange1, lp_orange2)
lap_orange1 = cv2.subtract(orange, lp_orange1)



# join the halves of their laplacian
cols1, rows1, chn1 = lap_apple1.shape
cols2, rows2, chn2 = lap_apple2.shape

laplacian1 = np.hstack((lap_apple1[:, 0:int(cols1 // 2)], lap_orange1[:, int(cols1 // 2):]))
laplacian2 = np.hstack((lap_apple2[:, 0:int(cols2 // 2)], lap_orange2[:, int(cols2 // 2):]))

print(apple.shape)
print(laplacian1.shape)



# reconstruct by merging the joined laplacian halves with their upsampled versions
#apple_orange_reconstruct = cv2.pyrUp(laplacian)
apple_orange_re = cv2.pyrUp(laplacian2)

apple_orange_reconstruct2 = cv2.add(laplacian1, apple_orange_re)
apple_orange_reconstruct1 = cv2.add(apple_orange, laplacian1)



cv2.imshow('apple', apple)
cv2.imshow('orange', orange)
cv2.imshow('apple_orange', apple_orange)
cv2.imshow('laplacian2', laplacian2)
cv2.imshow('laplacian1', laplacian1)
cv2.imshow('apple_orange_reconstruct2', apple_orange_reconstruct2)
cv2.imshow('apple_orange_reconstruct1', apple_orange_reconstruct1)


cv2.waitKey(0)
cv2.destroyAllWindows()
