import os
import cv2 as cv

img = cv.imread(os.path.join('.','persons-bike.jpg'))

print(img.shape)

resized_image = cv.resize(img, (600, 800))  # (Width, Height)

print(resized_image.shape)  # (Height, Width, Channel)

cv.imshow('Frame', resized_image)
cv.waitKey(0)
cv.destroyAllWindows()