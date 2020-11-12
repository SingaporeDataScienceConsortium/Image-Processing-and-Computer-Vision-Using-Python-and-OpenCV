# The code is shared on SDSC Github

import cv2 as cv
import numpy as np

fruit = cv.imread("../data/fruits.jpg") # read image
h, w = fruit.shape[0:2] # get image height and width

changes = np.linspace(0, 360, num=100) # create sampling points (for 360 degrees)
for i in changes: # go through the sampling points
      T_matrix = cv.getRotationMatrix2D((w/2, h/2), i, 1) # get the rotation matrix
      fruit_new = cv.warpAffine(fruit, T_matrix, (w, h)) # apply translation
      cv.imshow('Fruit',fruit_new)
      cv.waitKey(50) # wait for 50ms

r = np.linspace(0, 290, num=100) # variable radius
for c, i in enumerate(changes):

      # define the translation matrix
      T_matrix = np.float32([[1, 0, r[c]*np.sin(i*np.pi/180)], [0, 1, r[c]*np.cos(i*np.pi/180)]])

      fruit_new = cv.warpAffine(fruit, T_matrix, (w, h)) # perform translation
      T_matrix = cv.getRotationMatrix2D((w/2, h/2), i, 1)
      fruit_new = cv.warpAffine(fruit_new, T_matrix, (w, h))
      cv.imshow('Fruit',fruit_new)
      cv.waitKey(50)

cv.waitKey() # wait for any key press
cv.destroyAllWindows() # close all windows

