# The code is shared on SDSC Github

import cv2 as cv
import numpy as np

fruit = cv.imread("../data/fruits.jpg") # read image
h, w = fruit.shape[0:2] # get image height and width

changes = np.linspace(100, 200, num=50) # create sampling points
for i in changes:
      pt1 = np.float32([[100, 100], [300, 100], [100, 300]]) # coordinates of 3 points before transformation
      pt2 = np.float32([[100, 100], [300, 100], [i, 300]]) # coordinates of 3 points after transformation
      T_matrix = cv.getAffineTransform(pt1, pt2) # determine the matrix for Affine transformation
      fruit_new = cv.warpAffine(fruit, T_matrix, (w, h)) # perform Affine transformation
      cv.imshow('Fruit',fruit_new)
      cv.waitKey(20) # wait for 20ms

changes = np.linspace(100, 400, num=100)
for i in changes:
      pt1 = np.float32([[100, 100], [300, 100], [100, 300]])
      pt2 = np.float32([[100, 100], [300, 100], [100, i]])
      T_matrix = cv.getAffineTransform(pt1, pt2)
      fruit_new = cv.warpAffine(fruit, T_matrix, (w, h))
      cv.imshow('Fruit',fruit_new)
      cv.waitKey(20)

changes = np.linspace(100, 400, num=100)
for i in changes:
      pt1 = np.float32([[100, 100], [300, 100], [100, 300]])
      pt2 = np.float32([[100, 100], [300, i], [100, 300]])
      T_matrix = cv.getAffineTransform(pt1, pt2)
      fruit_new = cv.warpAffine(fruit, T_matrix, (w, h))
      cv.imshow('Fruit',fruit_new)
      cv.waitKey(20)

changes = np.linspace(100, 400, num=100)
for i in changes:
      pt1 = np.float32([[100, 100], [300, 100], [100, 300]])
      pt2 = np.float32([[100, 100], [i, 100], [100, 300]])
      T_matrix = cv.getAffineTransform(pt1, pt2)
      fruit_new = cv.warpAffine(fruit, T_matrix, (w, h))
      cv.imshow('Fruit',fruit_new)
      cv.waitKey(20)

changes = np.linspace(100, 400, num=100)
for i in changes:
      pt1 = np.float32([[100, 100], [300, 100], [100, 300]])
      pt2 = np.float32([[100, i], [300, 100], [100, 300]])
      T_matrix = cv.getAffineTransform(pt1, pt2)
      fruit_new = cv.warpAffine(fruit, T_matrix, (w, h))
      cv.imshow('Fruit',fruit_new)
      cv.waitKey(20)

changes = np.linspace(100, 400, num=100)
for i in changes:
      pt1 = np.float32([[100, 100], [300, 100], [100, 300]])
      pt2 = np.float32([[i, 100], [300, 100], [100, 300]])
      T_matrix = cv.getAffineTransform(pt1, pt2)
      fruit_new = cv.warpAffine(fruit, T_matrix, (w, h))
      cv.imshow('Fruit',fruit_new)
      cv.waitKey(20)

cv.waitKey() # wait for any key press
cv.destroyAllWindows() # close all windows

