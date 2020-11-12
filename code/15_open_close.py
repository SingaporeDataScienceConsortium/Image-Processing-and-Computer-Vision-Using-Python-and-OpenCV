# The code is shared on SDSC Github

import cv2 as cv
from matplotlib import pyplot as plt

verification = cv.imread('../data/verification.jpg') # read image
verification = cv.cvtColor(verification, cv.COLOR_BGR2GRAY) # convert from BGR to GRAY

# image binarization using Otsu's method
re, verification = cv.threshold(verification, 0, 255, cv.THRESH_BINARY_INV | cv.THRESH_OTSU)

plt.subplot(241) # create panel (2 rows and 4 columns) and locate to the first sub-figure
plt.imshow(verification, cmap = 'gray')
plt.title('Original') # title
plt.xticks([]) # remove x axis
plt.yticks([]) # remove y axis

open_filter = cv.getStructuringElement(cv.MORPH_RECT, (5, 5)) # define a filter for opening
opened = cv.morphologyEx(verification, cv.MORPH_OPEN, open_filter) # perform opening
plt.subplot(242)
plt.imshow(opened, cmap = 'gray')
plt.title('Open')
plt.xticks([])
plt.yticks([])

open_filter = cv.getStructuringElement(cv.MORPH_RECT, (1, 3))
opened = cv.morphologyEx(verification, cv.MORPH_OPEN, open_filter)
plt.subplot(243)
plt.imshow(opened, cmap = 'gray')
plt.title('Open (Remove horizontal lines)')
plt.xticks([])
plt.yticks([])

open_filter = cv.getStructuringElement(cv.MORPH_RECT, (3, 1))
opened = cv.morphologyEx(verification, cv.MORPH_OPEN, open_filter)
plt.subplot(244)
plt.imshow(opened, cmap = 'gray')
plt.title('Open (Remove vertical lines)')
plt.xticks([])
plt.yticks([])

fruit_noise = cv.imread('../data/line_noise.jpg')
plt.subplot(245)
plt.imshow(cv.cvtColor(fruit_noise, cv.COLOR_BGR2RGB))
plt.title('Original')
plt.xticks([])
plt.yticks([])

close_filter = cv.getStructuringElement(cv.MORPH_RECT, (3, 3)) # define a filter for closing
fruit = cv.morphologyEx(fruit_noise, cv.MORPH_CLOSE, close_filter) # perform opening
plt.subplot(246)
plt.imshow(cv.cvtColor(fruit, cv.COLOR_BGR2RGB))
plt.title('Close (Remove line noise)')
plt.xticks([])
plt.yticks([])

spiral_noise = cv.imread('../data/spiral.jpg')
spiral_noise = cv.cvtColor(spiral_noise, cv.COLOR_BGR2GRAY)
re, spiral_noise = cv.threshold(spiral_noise, 0, 255, cv.THRESH_BINARY_INV | cv.THRESH_OTSU)

plt.subplot(247)
plt.imshow(spiral_noise, cmap = 'gray')
plt.title('Original')
plt.xticks([])
plt.yticks([])

close_filter = cv.getStructuringElement(cv.MORPH_RECT, (9, 9))
spiral = cv.morphologyEx(spiral_noise, cv.MORPH_CLOSE, close_filter)
plt.subplot(248)
plt.imshow(spiral, cmap = 'gray')
plt.title('Close (Remove line noise)')
plt.xticks([])
plt.yticks([])





