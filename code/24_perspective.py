# The code is shared on SDSC Github

import cv2 as cv
import numpy as np

fruit = cv.imread("../data/fruits.jpg") # read image
h, w = fruit.shape[0:2] # get image height and width

changes = np.linspace(100, 200, num=50) # create sampling points
for i in changes:
      pt1 = np.float32([[0, 0], [200, 0], [0, 200], [200, 200]]) # coordinates of 4 points before transformation
      pt2 = np.float32([[0, 0], [200, 0], [0, 200], [200, i]]) # coordinates of 4 points after transformation
      T_matrix = cv.getPerspectiveTransform(pt1, pt2) # determine the matrix for perspective transformation
      fruit_new = cv.warpPerspective(fruit, T_matrix, (w, h)) # perform Affine transformation
      cv.imshow('Fruit',fruit_new)
      cv.waitKey(20) # wait for 20ms

changes = np.linspace(100, 200, num=50)
for i in changes:
      pt1 = np.float32([[0, 0], [200, 0], [0, 200], [200, 200]])
      pt2 = np.float32([[0, 0], [200, 0], [0, 200], [i, 200]])
      T_matrix = cv.getPerspectiveTransform(pt1, pt2)
      fruit_new = cv.warpPerspective(fruit, T_matrix, (w, h))
      cv.imshow('Fruit',fruit_new)
      cv.waitKey(20)

changes = np.linspace(100, 200, num=50)
for i in changes:
      pt1 = np.float32([[0, 0], [200, 0], [0, 200], [200, 200]])
      pt2 = np.float32([[0, 0], [200, 0], [0, i], [200, 200]])
      T_matrix = cv.getPerspectiveTransform(pt1, pt2)
      fruit_new = cv.warpPerspective(fruit, T_matrix, (w, h))
      cv.imshow('Fruit',fruit_new)
      cv.waitKey(20)

changes = np.linspace(100, 200, num=50)
for i in changes:
      pt1 = np.float32([[0, 0], [200, 0], [0, 200], [200, 200]])
      pt2 = np.float32([[0, 0], [200, 0], [i, 200], [200, 200]])
      T_matrix = cv.getPerspectiveTransform(pt1, pt2)
      fruit_new = cv.warpPerspective(fruit, T_matrix, (w, h))
      cv.imshow('Fruit',fruit_new)
      cv.waitKey(20)

changes = np.linspace(100, 200, num=50)
for i in changes:
      pt1 = np.float32([[0, 0], [200, 0], [0, 200], [200, 200]])
      pt2 = np.float32([[0, 0], [200, i], [0, 200], [200, 200]])
      T_matrix = cv.getPerspectiveTransform(pt1, pt2)
      fruit_new = cv.warpPerspective(fruit, T_matrix, (w, h))
      cv.imshow('Fruit',fruit_new)
      cv.waitKey(20)

changes = np.linspace(100, 200, num=50)
for i in changes:
      pt1 = np.float32([[0, 0], [200, 0], [0, 200], [200, 200]])
      pt2 = np.float32([[0, 0], [i, 0], [0, 200], [200, 200]])
      T_matrix = cv.getPerspectiveTransform(pt1, pt2)
      fruit_new = cv.warpPerspective(fruit, T_matrix, (w, h))
      cv.imshow('Fruit',fruit_new)
      cv.waitKey(20)

changes = np.linspace(100, 200, num=50)
for i in changes:
      pt1 = np.float32([[0, 0], [200, 0], [0, 200], [200, 200]])
      pt2 = np.float32([[0, i], [200, 0], [0, 200], [200, 200]])
      T_matrix = cv.getPerspectiveTransform(pt1, pt2)
      fruit_new = cv.warpPerspective(fruit, T_matrix, (w, h))
      cv.imshow('Fruit',fruit_new)
      cv.waitKey(20)

changes = np.linspace(100, 200, num=50)
for i in changes:
      pt1 = np.float32([[0, 0], [200, 0], [0, 200], [200, 200]])
      pt2 = np.float32([[i, 0], [200, 0], [0, 200], [200, 200]])
      T_matrix = cv.getPerspectiveTransform(pt1, pt2)
      fruit_new = cv.warpPerspective(fruit, T_matrix, (w, h))
      cv.imshow('Fruit',fruit_new)
      cv.waitKey(20)

cv.waitKey() # wait for any key press
cv.destroyAllWindows() # close all windows

