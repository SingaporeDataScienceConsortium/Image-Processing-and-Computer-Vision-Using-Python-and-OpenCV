# The code is shared on SDSC Github

import cv2 as cv
import numpy as np

hand_written_numbers = cv.imread("../data/hand_written_numbers.jpg") # read image
cv.imshow("Original", hand_written_numbers)

GrayImg = cv.cvtColor(hand_written_numbers, cv.COLOR_BGR2GRAY) # convert from BGR to GRAY

# image binarization using Otsu's method
ret, BinaryImg = cv.threshold(GrayImg, 0, 255, cv.THRESH_BINARY_INV | cv.THRESH_OTSU)

# detect object contours of the binary image
contours_info, zz = cv.findContours(BinaryImg, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)

for i, contour in enumerate(contours_info): # go through each contour
      x, y, width, height = cv.boundingRect(contour) # get the  top-left coordinate, width and height
      moments = cv.moments(contour) # object moments
      center_x = moments['m10']/moments['m00'] # x position
      center_y = moments['m01']/moments['m00'] # y position
      cv.circle(hand_written_numbers, (np.int(center_x), np.int(center_y)), 2, (0, 255, 255), -1) # draw the center
      cv.rectangle(hand_written_numbers, (x, y), (x+width, y+height), (0, 0, 255), 2) # draw a box enclosing the object
cv.imshow("measure-contours", hand_written_numbers)

cv.waitKey(0) # wait for any key press
cv.destroyAllWindows() # close all windows

