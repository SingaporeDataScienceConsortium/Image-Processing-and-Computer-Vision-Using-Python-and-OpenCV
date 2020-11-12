# The code is shared on SDSC Github

import cv2 as cv
from matplotlib import pyplot as plt

number = cv.imread('../data/8.jpg') # read image
number = cv.cvtColor(number, cv.COLOR_BGR2GRAY) # convert from BGR to GRAY

# image binarization using Otsu's method
re, number = cv.threshold(number, 0, 255, cv.THRESH_BINARY_INV | cv.THRESH_OTSU)

plt.subplot(241) # create panel (2 rows and 4 columns) and locate to the first sub-figure
plt.imshow(number, cmap = 'gray')
plt.title('Original') # title
plt.xticks([]) # remove x axis
plt.yticks([]) # remove y axis

filter_size = [3, 5, 7] # sizes of eroding filter
for c,i in enumerate(filter_size): # use different filters
    erode_filter = cv.getStructuringElement(cv.MORPH_RECT, (i, i)) # construct a filter
    erode = cv.erode(number, erode_filter) # perform erosion
    plt.subplot(2, 4, c+2)
    plt.imshow(erode, cmap = 'gray')
    plt.title('Erode filter ' +  str(i))
    plt.xticks([])
    plt.yticks([])

filter_size = [3, 5, 7, 9] # sizes of dilating filter
for c,i in enumerate(filter_size): # use different filters
    dilate_filter = cv.getStructuringElement(cv.MORPH_RECT, (i, i)) # construct a filter
    dilate = cv.dilate(number, dilate_filter) # perform dilation
    plt.subplot(2, 4, c+5)
    plt.imshow(dilate, cmap = 'gray')
    plt.title('Dilate filter ' +  str(i))
    plt.xticks([])
    plt.yticks([])
