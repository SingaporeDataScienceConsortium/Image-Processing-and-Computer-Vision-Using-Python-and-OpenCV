# The code is shared on SDSC Github

import cv2 as cv
import numpy as np

fruit = cv.imread("../data/fruits.jpg") # read image

changes = np.linspace(0.2, 1, num=100) # create sampling points
for i in changes: # go through each of the sampling point
      fruit_new = cv.resize(fruit, None, fx=i, fy=1-i+0.2, interpolation = cv.INTER_AREA) # resize image
      cv.imshow('Fruit',fruit_new)
      cv.waitKey(50) # wait for 50ms
cv.destroyAllWindows() # close all windows

changes = np.linspace(0.2, 1, num=100)
for i in changes:
      w = np.uint(i*fruit.shape[1])
      h = np.uint((1-i+0.2)*fruit.shape[0])
      fruit_new = cv.resize(fruit, (w, h), interpolation = cv.INTER_AREA)
      cv.imshow('Fruit',fruit_new)
      cv.waitKey(50)
cv.destroyAllWindows()

