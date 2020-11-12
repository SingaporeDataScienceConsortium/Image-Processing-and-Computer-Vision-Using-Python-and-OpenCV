# The code is shared on SDSC Github

import cv2 as cv

img1 = cv.imread('../data/1.jpg') # read image 1
img2 = cv.imread('../data/2.jpg') # read image 2

stitcher = cv.Stitcher_create() # initialize a stitcher
_, combine = stitcher.stitch((img1, img2)) # perform stitching

cv.imshow('Result',combine)

cv.waitKey(0) # wait for any key press
cv.destroyAllWindows() # close all windows


