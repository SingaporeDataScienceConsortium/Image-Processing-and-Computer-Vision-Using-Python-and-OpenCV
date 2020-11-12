# The code is shared on SDSC Github

import cv2 as cv
from matplotlib import pyplot as plt

Cologne = cv.imread('../data/Cologne.jpg') # read image
Cologne_HSV = cv.cvtColor(Cologne, cv.COLOR_BGR2HSV) # convert from BGR to HSV
Cologne_HSV[:, :, 2] = cv.equalizeHist(Cologne_HSV[:, :, 2]) # normalize the VALUE channel

plt.subplot(2, 2, 1) # create panel (2 rows and 2 columns) and locate to the first sub-figure
plt.imshow(cv.cvtColor(Cologne, cv.COLOR_BGR2RGB)) # convert from BGR to RGB
plt.title('Original') # title
plt.xticks([]) # remove x axis
plt.yticks([]) # remove y axis

plt.subplot(2, 2, 2)
plt.imshow(cv.cvtColor(Cologne_HSV, cv.COLOR_HSV2RGB)) # convert from HSV to RGB
plt.title('After hist normalized')
plt.xticks([])
plt.yticks([])


Ball = cv.imread('../data/Ball.jpg')
Ball_HSV = cv.cvtColor(Ball, cv.COLOR_BGR2HSV) # convert from BGR to HSV
Ball_HSV[:, :, 2] = cv.equalizeHist(Ball_HSV[:, :, 2]) # normalize the VALUE channel

plt.subplot(2, 2, 3)
plt.imshow(cv.cvtColor(Ball, cv.COLOR_BGR2RGB)) # convert from BGR to RGB
plt.title('Original')
plt.xticks([])
plt.yticks([])

plt.subplot(2, 2, 4)
plt.imshow(cv.cvtColor(Ball_HSV, cv.COLOR_HSV2RGB)) # convert from HSV to RGB
plt.title('After hist normalized')
plt.xticks([])
plt.yticks([])