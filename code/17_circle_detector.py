# The code is shared on SDSC Github

import cv2 as cv

coins = cv.imread("../data/coins.jpg") # read image
cv.imshow("Original", coins)

coins_detect = cv.cvtColor(coins, cv.COLOR_BGR2GRAY) # convert from BGR to GRAY
coins_detect = cv.GaussianBlur(coins_detect, (31,31),0)

# perform Hough circle detection
circle_info = cv.HoughCircles(coins_detect, cv.HOUGH_GRADIENT, 1, 20, param1=50, param2=30)

for i in circle_info[0, :]: # go through the information of each circle
      cv.circle(coins, (i[0], i[1]), i[2], (0, 0, 255), 2) # draw the contour of each circle
      cv.circle(coins, (i[0], i[1]), 2, (255, 0, 0), 2) # draw the center of each circle
cv.imshow("Circle Detector", coins)

cv.waitKey(0) # wait for any key press
cv.destroyAllWindows() # close all windows

