# Import libraries
import os
import cv2 as cv

# Images
# --------------------------------------------------------------------------
# Read image
image_path = os.path.join('.', 'sample.jpg')

# imread() - used for reading images from files into NumPy arrays
img = cv.imread(image_path)

# Write image
cv.imwrite(os.path.join('.', 'sample_out.jpg'), img)

# Open image
cv.imshow('Image Viewer',img)
cv.waitKey(0)   # Used to keep the frame 0-indefinitely, else time is ms

# --------------------------------------------------------------------

# Videos
# --------------------------------------------------------------------

# read video
video_path = os.path.join('.', 'sample_video.mp4')

video = cv.VideoCapture(video_path)

# Visualize video

times = True
while times:
    times, frame = video.read()
    cv.imshow('Video Frame', frame)
    cv.waitKey(40)
video.release()
cv.destroyAllWindows()

# --------------------------------------------------------------------------
# Webcam
# --------------------------------------------------------------------------

webcam = cv.VideoCapture(0)

# Open web cam
while True:
    ret, frame = webcam.read()

    cv.imshow('Webcam Frame', frame)
    if cv2.waitKey(10) & 0xFF == ord('q'):
        break

webcam.release()
cv.destroyAllWindows()
