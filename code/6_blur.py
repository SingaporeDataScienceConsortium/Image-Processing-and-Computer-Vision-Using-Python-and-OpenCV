# The code is shared on SDSC Github

import cv2 as cv
from matplotlib import pyplot as plt

fruit = cv.imread('../data/fruits.jpg') # read image

levels = [1, 4, 7, 10, 13] # define filter sizes (size of the normalized box filter)
for c, i in enumerate(levels):
    BlurImg = cv.blur(fruit,(i,i)) # blur each image
    plt.subplot(4, 5, c+1) # create panel (4 rows and 5 columns) and locate to the first row of sub-figures
    plt.imshow(cv.cvtColor(BlurImg, cv.COLOR_BGR2RGB)) # convert from BGR to RGB
    plt.title('Average '+str(i)) # title
    plt.xticks([]) # remove x axis
    plt.yticks([]) # remove y axis

levels = [1, 5, 9, 13, 17] # define filter sizes (size of the median filter)
for c, i in enumerate(levels):
    BlurImg = cv.medianBlur(fruit,i)
    plt.subplot(4, 5, 5+c+1)
    plt.imshow(cv.cvtColor(BlurImg, cv.COLOR_BGR2RGB))
    plt.title('Median '+str(i))
    plt.xticks([])
    plt.yticks([])

levels = [1, 5, 9, 13, 17] # define filter sizes (size of the Gaussian filter)
for c, i in enumerate(levels):
    BlurImg = cv.GaussianBlur(fruit, (i,i),0)
    plt.subplot(4, 5, 10+c+1)
    plt.imshow(cv.cvtColor(BlurImg, cv.COLOR_BGR2RGB))
    plt.title('Gaussian '+str(i))
    plt.xticks([])
    plt.yticks([])

