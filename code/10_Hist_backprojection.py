# The code is shared on SDSC Github

import cv2 as cv
from matplotlib import pyplot as plt

football = cv.imread('../data/football.jpeg') # read the image
jersey = cv.imread('../data/jersey_color.jpeg') # read the feature image

plt.subplot(231) # create panel (2 rows and 3 columns) and locate to the first sub-figure
plt.imshow(cv.cvtColor(football, cv.COLOR_BGR2RGB)) # convert from BGR to RGB
plt.title('Image') # title
plt.xticks([]) # remove x axis
plt.yticks([]) # remove y axis

plt.subplot(234) # create panel (2 rows and 3 columns) and locate to the fourth sub-figure
plt.imshow(cv.cvtColor(jersey, cv.COLOR_BGR2RGB))
plt.title('ROI')
plt.xticks([])
plt.yticks([])

football_HSV = cv.cvtColor(football, cv.COLOR_BGR2HSV) # convert from BGR to HSV
jersey_HSV = cv.cvtColor(jersey, cv.COLOR_BGR2HSV)

# bins = 180, 256

# calculate the histogram of the feature image
jersey_Hist = cv.calcHist([jersey_HSV], [0, 1], None, [180, 256], [0, 180, 0, 256])

# get the result backprojection
BackProject = cv.calcBackProject([football_HSV], [0, 1], jersey_Hist, [0, 180, 0, 256], 1)
plt.subplot(232)
plt.imshow(BackProject, cmap = 'gray')
plt.title('Bins = 180, 256')
plt.xticks([])
plt.yticks([])

# bins = 90, 128
jersey_Hist = cv.calcHist([jersey_HSV], [0, 1], None, [90, 128], [0, 180, 0, 256])

BackProject = cv.calcBackProject([football_HSV], [0, 1], jersey_Hist, [0, 180, 0, 256], 1)
plt.subplot(233)
plt.imshow(BackProject, cmap = 'gray')
plt.title('Bins = 90, 128')
plt.xticks([])
plt.yticks([])

# bins = 45, 64
jersey_Hist = cv.calcHist([jersey_HSV], [0, 1], None, [45, 64], [0, 180, 0, 256])

BackProject = cv.calcBackProject([football_HSV], [0, 1], jersey_Hist, [0, 180, 0, 256], 1)
plt.subplot(235)
plt.imshow(BackProject, cmap = 'gray')
plt.title('Bins = 45, 64')
plt.xticks([])
plt.yticks([])

# bins = 45, 64
jersey_Hist = cv.calcHist([jersey_HSV], [0, 1], None, [22, 32], [0, 180, 0, 256])

BackProject = cv.calcBackProject([football_HSV], [0, 1], jersey_Hist, [0, 180, 0, 256], 1)

plt.subplot(236)
plt.imshow(BackProject, cmap = 'gray')
plt.title('Bins = 22, 32')
plt.xticks([])
plt.yticks([])







