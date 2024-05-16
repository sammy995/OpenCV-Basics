import cv2 as cv
import os

# Read image
img = cv.imread(os.path.join('.', 'persons-bike.jpg'))

img_gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

"""Threshold = technique to separate regions of an image based on intensity levels. 
It is commonly used for image segmentation, where it divides an image into a binary image (black and white) 
based on a threshold value.
"""
retval, img_thresh = cv.threshold(img_gray, thresh=80, maxval=255, type=cv.THRESH_BINARY)

"""
retval -> thresh value that was used
thresh -> If the pixel value is greater than the threshold, it is set to maxval; otherwise, it is set to 0.
THRESH_BINARY -> if val > thresh then Maxval else 0
THRESH_BINARY_INV -> if val > thresh then 0 else maxval
THRESH_TRUNC -> if val > thresh then thresh else noChange
THRESH_TOZERO -> if val > thresh then 0 else noChange
THRESH_TOZERO_INV -> if val < thresh then Maxval else noChange
"""

# Adaptive threshold

adaptive_img = cv.adaptiveThreshold(img_gray, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, 21, 30)


cv.imshow('Gray image', img_gray)
cv.imshow('Simple Threshold image', img_thresh)
cv.imshow('Adaptive Threshold image', adaptive_img)
cv.waitKey(0)
cv.destroyAllWindows()