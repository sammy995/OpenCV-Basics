import cv2 as cv
import os


# Read image
img = cv.imread(os.path.join('.', 'sample_out_cropped.jpg'))

# Draw Line
cv.line(img, pt1=(100,150), pt2=(300,600), color=(255,0,0),thickness= 4)

# Draw Rectangle
cv.rectangle(img, pt1=(50,50),pt2=(100,200),color=(0,0,255),thickness=-1)

# Draw Circle
cv.circle(img, radius=70, center=(190,80),color=(200,255,100), thickness=7)

# Draw Text
cv.putText(img,
           text="A sentinal", org=(0,500),
           fontFace=cv.FONT_HERSHEY_DUPLEX, fontScale=1.5,
           color=(0,0,0), thickness=8)

cv.imshow('Original image', img)
cv.waitKey(0)
cv.destroyAllWindows()