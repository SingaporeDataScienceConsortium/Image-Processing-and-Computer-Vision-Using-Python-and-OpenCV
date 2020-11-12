# The code is shared on SDSC Github

import cv2 as cv
from matplotlib import pyplot as plt

Cologne = cv.imread('../data/Cologne.jpg') # read image
Cologne_RGB = cv.cvtColor(Cologne, cv.COLOR_BGR2RGB) # convert from BGR to RGB
Cologne_RGB[:, :, 0] = cv.equalizeHist(Cologne_RGB[:, :, 0]) # normalize channel 1 - Red
Cologne_RGB[:, :, 1] = cv.equalizeHist(Cologne_RGB[:, :, 1]) # normalize channel 2 - Green
Cologne_RGB[:, :, 2] = cv.equalizeHist(Cologne_RGB[:, :, 2]) # normalize channel 3 - Blue

plt.subplot(2, 2, 1) # create panel (2 rows and 2 columns) and locate to the first sub-figure
plt.imshow(cv.cvtColor(Cologne, cv.COLOR_BGR2RGB)) # convert from BGR to RGB
plt.title('Original') # title
plt.xticks([]) # remove x axis
plt.yticks([]) # remove y axis

plt.subplot(2, 2, 2)
plt.imshow(Cologne_RGB)
plt.title('After hist normalized')
plt.xticks([])
plt.yticks([])

Ball = cv.imread('../data/Ball.jpg')
Ball_RGB = cv.cvtColor(Ball, cv.COLOR_BGR2RGB)
Ball_RGB[:, :, 0] = cv.equalizeHist(Ball_RGB[:, :, 0])
Ball_RGB[:, :, 1] = cv.equalizeHist(Ball_RGB[:, :, 1])
Ball_RGB[:, :, 2] = cv.equalizeHist(Ball_RGB[:, :, 2])

plt.subplot(2, 2, 3)
plt.imshow(cv.cvtColor(Ball, cv.COLOR_BGR2RGB))
plt.title('Original')
plt.xticks([])
plt.yticks([])

plt.subplot(2, 2, 4)
plt.imshow(Ball_RGB)
plt.title('After hist normalized')
plt.xticks([])
plt.yticks([])