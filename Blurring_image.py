import cv2 as cv
import os

# Read image
img = cv.imread(os.path.join('.', 'persons-bike.jpg'))

"""
blurring is a common technique used to reduce noise and detail in images. 
It helps in preprocessing images before performing further operations like edge detection or object recognition.
 
 Functions:
 1. blur() - This function applies a simple averaging filter to the image. Also called box filter. 
 It takes the average of all pixels under the kernel area and replaces the central pixel with this average
 
 2. GaussianBlur(): This function applies a Gaussian blur to the image. 
 It uses a Gaussian kernel which gives more weight to the central pixels while averaging 
 
 3. medianBlur(): This function applies a median filter to the image. 
 It replaces each pixel's value with the median value of the pixels in its neighborhood.
  
 4. bilateralFilter(): This function applies a bilateral filter to the image. It preserves edges while reducing noise. 
  It takes into account both the spatial distance and intensity difference when filtering."""

# Blur Image
k_size = 9 # Kernel size. Larger the number higher the blur
blurred_img_blur = cv.blur(img, (k_size,k_size))
blurred_img_gaussian = cv.GaussianBlur(img, ksize=(k_size,k_size), sigmaX=3, sigmaY=2)
blurred_img_median = cv.medianBlur(img, k_size)

cv.imshow('Original image', img)
cv.imshow('Blur image', blurred_img_blur)
cv.imshow('Gaussian Blur image', blurred_img_gaussian)
cv.imshow('Median Blur image', blurred_img_median)

cv.waitKey(0)
cv.destroyAllWindows()