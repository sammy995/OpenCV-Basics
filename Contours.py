import cv2 as cv
import os


# Read image
img = cv.imread(os.path.join('.', 'birds.jpg'))
resized_image = cv.resize(img, (800, 600))
img_gray = cv.cvtColor(resized_image, cv.COLOR_RGB2GRAY)

retval, thresh_img = cv.threshold(img_gray, 127, 255, cv.THRESH_BINARY_INV)

# Contours -Contours are curves joining continuous points along the boundary of an object in an image.
# They are useful for shape analysis, object detection, and object recognition tasks.

contours, hierarchy = cv.findContours(thresh_img, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)

"""
Parameters:
image: Input image (numpy.ndarray). It should be a binary image.
mode: Contour retrieval mode. It specifies how contours are retrieved from the image. It can be one of the following:
    cv2.RETR_EXTERNAL: Retrieves only the external contours.
    cv2.RETR_LIST: Retrieves all contours without any hierarchical relationships.
    cv2.RETR_CCOMP: Retrieves all contours and organizes them into a two-level hierarchy. External contours are in the top-level hierarchy, and holes are in the second level.
    cv2.RETR_TREE: Retrieves all contours and reconstructs a full hierarchy of nested contours.
method: Contour approximation method. It specifies how the contour points are approximated. It can be one of the following:
    cv2.CHAIN_APPROX_NONE: Stores all the contour points. This can be memory-intensive.
    cv2.CHAIN_APPROX_SIMPLE: Compresses horizontal, vertical, and diagonal segments and leaves only their end points.
    cv2.CHAIN_APPROX_TC89_L1: Applies the Teh-Chin chain approximation algorithm.
    cv2.CHAIN_APPROX_TC89_KCOS: Applies the Teh-Chin chain approximation algorithm to remove redundant points.
offset: Optional offset added to the retrieved contours.

Return Values:
contours: A list of contours found in the image. Each contour is represented 
          as a numpy array of (x, y) coordinates of the contour points.
hierarchy: Optional output containing information about the hierarchical relationships between contours. 
           It is useful when using cv2.RETR_CCOMP or cv2.RETR_TREE modes.
"""
# Get all contours and draw bounding box around the contour
for c in contours:
    if cv.contourArea(c) > 127:
        #cv.drawContours(resized_image,c, -1, color=(0, 255, 0), thickness=2)
        x1, y1, w, h = cv.boundingRect(c)
        cv.rectangle(resized_image, (x1,y1),(x1+w, y1+h), (0,255,0),2)

cv.imshow('Bounding box', resized_image)
cv.waitKey(0)
cv.destroyAllWindows()