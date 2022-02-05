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

print(apple.shape)
print(orange.shape)

# generate gaus pyramid for apple
gaus_apple = cv2.pyrDown(apple)

# generate gaus pyramid for orange
gaus_orange = cv2.pyrDown(orange)

# generate laplacian pyramid for apple
lp_apple = cv2.pyrUp(gaus_apple)
lap_apple = cv2.subtract(apple, lp_apple)

# generate laplacian pyramid for orange
lp_orange = cv2.pyrUp(gaus_orange)
lap_orange = cv2.subtract(orange, lp_orange)

# join the halves of their laplacian
cols, rows, chn = lap_apple.shape
laplacian = np.hstack((lap_apple[:, 0:int(cols // 2)], lap_orange[:, int(cols // 2):]))

# reconstruct by merging the joined laplacian halves with their upsampled versions
#apple_orange_reconstruct = cv2.pyrUp(laplacian)
apple_orange_reconstruct = cv2.add(apple_orange, laplacian)


cv2.imshow('apple', apple)
cv2.imshow('orange', orange)
cv2.imshow('apple_orange', apple_orange)
cv2.imshow('laplacian', laplacian)
cv2.imshow('apple_orange_reconstruct', apple_orange_reconstruct)

cv2.waitKey(0)
cv2.destroyAllWindows()
