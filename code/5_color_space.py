# The code is shared on SDSC Github

import cv2 as cv

fruit = cv.imread('../data/fruits.jpg') # read image

BGR = fruit
cv.imshow("BGR", BGR)

GRAY = cv.cvtColor(fruit, cv.COLOR_BGR2GRAY) # convert from BGR to GRAY
cv.imshow("GRAY", GRAY)

HSV = cv.cvtColor(fruit, cv.COLOR_BGR2HSV) # convert from BGR to HSV
cv.imshow("HSV", HSV)

YUV = cv.cvtColor(fruit, cv.COLOR_BGR2YUV) # convert from BGR to YUV
cv.imshow("YUV", YUV)

RGB = cv.cvtColor(fruit, cv.COLOR_BGR2RGB) # convert from BGR to RGB
cv.imshow("RGB", RGB)

cv.waitKey(0) # wait for any key press
cv.destroyAllWindows() # close all windows

