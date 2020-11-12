# The code is shared on SDSC Github

import cv2 as cv
import numpy as np

fruit = cv.imread("../data/fruits.jpg") # read image
h, w = fruit.shape[0:2] # get image height and width

changes = np.linspace(0, 359, num=100) # create sampling points (for 360 degrees)
r = 200 # fixed radius
for i in changes: # go through the sampling points

      # create a transformation matrix
      T_matrix = np.float32([[1, 0, r*np.sin(i*np.pi/180)], [0, 1, r*np.cos(i*np.pi/180)]])

      fruit_new = cv.warpAffine(fruit, T_matrix, (w, h)) # apply translation
      cv.imshow('Fruit',fruit_new)
      cv.waitKey(50) # wait for 50ms

changes = np.linspace(0, 359, num=100)
r = np.linspace(0, 290, num=100) # variable radius
for c, i in enumerate(changes):
      T_matrix = np.float32([[1, 0, r[c]*np.sin(i*np.pi/180)], [0, 1, r[c]*np.cos(i*np.pi/180)]])

      fruit_new = cv.warpAffine(fruit, T_matrix, (w, h))
      cv.imshow('Fruit',fruit_new)
      cv.waitKey(50)

cv.waitKey() # wait for any key press
cv.destroyAllWindows() # close all windows



