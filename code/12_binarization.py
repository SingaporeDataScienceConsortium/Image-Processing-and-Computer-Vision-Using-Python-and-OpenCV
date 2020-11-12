# The code is shared on SDSC Github

import cv2 as cv
from matplotlib import pyplot as plt
import numpy as np

embryo = cv.imread('../data/embryo.jpg') # read image
embryo = cv.cvtColor(embryo, cv.COLOR_BGR2GRAY) # convert from BGR to GRAY

re, binary = cv.threshold(embryo, 50, 255, cv.THRESH_BINARY) # image binarization using a defined threshold
plt.subplot(231) # create panel (2 rows and 3 columns) and locate to the first sub-figure
plt.imshow(binary, cmap = 'gray')
plt.title('Threshold = 50 (0~255)') # title
plt.xticks([]) # remove x axis
plt.yticks([]) # remove y axis

re, binary = cv.threshold(embryo, 100, 255, cv.THRESH_BINARY) # image binarization using a defined threshold
plt.subplot(232)
plt.imshow(binary, cmap = 'gray')
plt.title('Threshold = 100 (0~255)')
plt.xticks([])
plt.yticks([])

re, binary = cv.threshold(embryo, 150, 255, cv.THRESH_BINARY) # image binarization using a defined threshold
plt.subplot(233)
plt.imshow(binary, cmap = 'gray')
plt.title('Threshold = 150 (0~255)')
plt.xticks([])
plt.yticks([])

re, binary = cv.threshold(embryo, np.mean(embryo), 255, cv.THRESH_BINARY) # image binarization using the mean intensity
plt.subplot(234)
plt.imshow(binary, cmap = 'gray')
plt.title('Threshold = Mean (0~255)')
plt.xticks([])
plt.yticks([])

re, binary = cv.threshold(embryo, np.median(embryo), 255, cv.THRESH_BINARY) # image binarization using the median intensity
plt.subplot(235)
plt.imshow(binary, cmap = 'gray')
plt.title('Threshold = Median (0~255)')
plt.xticks([])
plt.yticks([])

re, binary = cv.threshold(embryo, 0, 255, cv.THRESH_BINARY | cv.THRESH_OTSU) # image binarization using Otsu's method
plt.subplot(236)
plt.imshow(binary, cmap = 'gray')
plt.title('Otsu Method')
plt.xticks([])
plt.yticks([])


