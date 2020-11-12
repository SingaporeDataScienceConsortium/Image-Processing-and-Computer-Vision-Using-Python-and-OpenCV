# The code is shared on SDSC Github

import cv2 as cv
import numpy as np

Sudoku = cv.imread("../data/Sudoku.jpg") # read image
cv.imshow("Original", Sudoku)

gray = cv.cvtColor(Sudoku, cv.COLOR_BGR2GRAY) # convert from BGR to GRAY
edge = cv.Canny(gray, 50, 100) # perform Canny edge detection
line_info = cv.HoughLines(edge, 1, np.pi/180, 200) # perform Hough transform
for line in line_info: # go through each detected line segment
    rho, theta = line[0] # extract the information of this line segment

    # define 2 points to draw a line over the image
    cos_value = np.cos(theta)
    sin_value = np.sin(theta)
    x_base = cos_value * rho
    y_base = sin_value * rho
    x1 = int(x_base+1500*(-sin_value))
    y1 = int(y_base+1500*(cos_value))
    x2 = int(x_base-1500*(-sin_value))
    y2 = int(y_base-1500*(cos_value))
    cv.line(Sudoku, (x1, y1), (x2, y2), (0, 0, 255), 1)

cv.imshow('Detected lines', Sudoku)
cv.waitKey(0) # wait for any key press
cv.destroyAllWindows() # close all windows


