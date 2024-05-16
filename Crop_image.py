import cv2 as cv
import os

# Read image
image_path = os.path.join('.', 'sample.jpg')

# imread() - used for reading images from files into NumPy arrays
img = cv.imread(image_path)

cropped_img = img[300:1000, 620:1000]

cv.imwrite(os.path.join('.', 'sample_out_cropped.jpg'), cropped_img)

cv.imshow('Cropped Image', cropped_img)
cv.waitKey(0)
cv.destroyAllWindows()