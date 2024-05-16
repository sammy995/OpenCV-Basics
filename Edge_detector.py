import cv2 as cv
import os

import numpy as np

# Read image
img = cv.imread(os.path.join('.', 'sample_out_cropped.jpg'))

# Edge detector
# It works by detecting areas of high gradient (intensity change) in the image, which typically correspond to edges.

edged_img = cv.Canny(img,threshold1= 100, threshold2= 420, apertureSize=3, L2gradient= True)
"""
threshold1: First threshold for the hysteresis procedure. This is used for edge linking.
threshold2: Second threshold for the hysteresis procedure. This is used for edge segment selection.
apertureSize: Aperture size for the Sobel operator (optional). Default is 3.
L2gradient: Flag indicating whether a more accurate L2 norm should be used to calculate image gradients (optional). 
Default is False, which uses the L1 norm.
"""

# Dilate Image - Dilation is a process that expands the boundaries of objects in an image. It is useful for accentuating
# features in an image and is often used in conjunction with other morphological operations like erosion, opening, and closing.

dilated_img = cv.dilate(edged_img, np.ones((4,4), dtype=np.int8))


cv.imshow('Original Image', img)
cv.imshow('Edge detector', edged_img)
cv.imshow('Dilated image', dilated_img)
cv.waitKey(0)
cv.destroyAllWindows()