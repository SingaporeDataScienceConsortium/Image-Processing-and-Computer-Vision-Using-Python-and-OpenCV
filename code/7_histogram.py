# The code is shared on SDSC Github

import cv2 as cv
from matplotlib import pyplot as plt

apple = cv.imread('../data/apple.jpg', cv.IMREAD_GRAYSCALE) # read image
apple_norm = cv.equalizeHist(apple) # equalize the histogram of the image

plt.subplot(2, 2, 1) # create panel (2 rows and 2 columns) and locate to the first sub-figure
plt.imshow(apple, cmap='gray') # display the image in gray
plt.title('Original') # title
plt.xticks([]) # remove x axis
plt.yticks([]) # remove y axis

plt.subplot(2, 2, 2)
plt.imshow(apple_norm, cmap='gray')
plt.title('After hist normalized')
plt.xticks([])
plt.yticks([])

plt.subplot(2, 2, 3)
plt.hist(apple.ravel(), 256, [0, 256]) # display the histogram of the image
plt.title('Histogram')
plt.xlabel('Grayscale') # x label
plt.ylabel('Count') # y label

plt.subplot(2, 2, 4)
plt.hist(apple_norm.ravel(), 256, [0, 256])
plt.title('Normalized histogram')
plt.xlabel('Grayscale')
plt.ylabel('Count')