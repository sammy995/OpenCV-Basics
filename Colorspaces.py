import cv2 as cv
import os

# Read image
img = cv.imread(os.path.join('.', 'sample_out_cropped.jpg'))

""" Convert colorspaces
cvtColor() = used for converting images from one color space to another. 
It is commonly used in image processing and computer vision applications to change the color representation of images.
"""
converted_image = cv.cvtColor(img, cv.COLOR_BGR2RGBA)
cv.imshow('Original Image', img)
cv.imshow('Converted Image', converted_image)
cv.waitKey(0)
cv.destroyAllWindows()

