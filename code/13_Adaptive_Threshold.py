# The code is shared on SDSC Github

import cv2 as cv
from matplotlib import pyplot as plt

Sudoku = cv.imread('../data/Sudoku.jpg') # read image
Sudoku = cv.cvtColor(Sudoku, cv.COLOR_BGR2GRAY) # convert from BGR to GRAY

plt.subplot(231) # create panel (2 rows and 3 columns) and locate to the first sub-figure
plt.imshow(Sudoku, cmap = 'gray')
plt.title('Original') # title
plt.xticks([]) # remove x axis
plt.yticks([]) # remove y axis

re, binary = cv.threshold(Sudoku, 50, 255, cv.THRESH_BINARY) # image binarization using a defined threshold
plt.subplot(232)
plt.imshow(binary, cmap = 'gray')
plt.title('Threshold = 50 (0~255)')
plt.xticks([])
plt.yticks([])

re, binary = cv.threshold(Sudoku, 100, 255, cv.THRESH_BINARY) # image binarization using a defined threshold
plt.subplot(233)
plt.imshow(binary, cmap = 'gray')
plt.title('Threshold = 100 (0~255)')
plt.xticks([])
plt.yticks([])

re, binary = cv.threshold(Sudoku, 150, 255, cv.THRESH_BINARY) # image binarization using a defined threshold
plt.subplot(234)
plt.imshow(binary, cmap = 'gray')
plt.title('Threshold = 150 (0~255)')
plt.xticks([])
plt.yticks([])

re, binary = cv.threshold(Sudoku, 0, 255, cv.THRESH_BINARY | cv.THRESH_OTSU) # image binarization using Otsu's method
plt.subplot(235)
plt.imshow(binary, cmap = 'gray')
plt.title('Otsu Method')
plt.xticks([])
plt.yticks([])

# image binarization using adaptive thresholding
binary = cv.adaptiveThreshold(Sudoku, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, 45, 10)

plt.subplot(236)
plt.imshow(binary, cmap = 'gray')
plt.title('Adaptive Threshold')
plt.xticks([])
plt.yticks([])


