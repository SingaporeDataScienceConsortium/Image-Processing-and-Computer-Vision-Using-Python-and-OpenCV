# The code is shared on SDSC Github

import cv2 as cv
from matplotlib import pyplot as plt

yao = cv.imread('../data/yao.jpg') # read image
plt.subplot(231) # create panel (2 rows and 3 columns) and locate to the first sub-figure
plt.imshow(cv.cvtColor(yao, cv.COLOR_BGR2RGB)) # convert from BGR to RGB
plt.title('Original') # title
plt.xticks([]) # remove x axis
plt.yticks([]) # remove y axis

plt.subplot(232)
plt.imshow(cv.cvtColor(yao, cv.COLOR_BGR2GRAY), cmap = 'gray')
plt.title('Gray')
plt.xticks([])
plt.yticks([])

Gx = cv.Sobel(yao, cv.CV_32F, 1, 0) # gradient x
Gy = cv.Sobel(yao, cv.CV_32F, 0, 1) # gradient y

G_x = cv.convertScaleAbs(Gx) # converting back to uint8
G_y = cv.convertScaleAbs(Gy) # converting back to uint8

G_xy = cv.addWeighted(G_x, 0.5, G_y, 0.5, 0) # calculates the weighted sum of two arrays

plt.subplot(233)
plt.imshow(G_x)
plt.title('Sobel X Grad')
plt.xticks([])
plt.yticks([])

plt.subplot(234)
plt.imshow(G_y)
plt.title('Sobel Y Grad')
plt.xticks([])
plt.yticks([])

plt.subplot(235)
plt.imshow(G_xy)
plt.title('Sobel XY Grad')
plt.xticks([])
plt.yticks([])

yao = cv.cvtColor(yao, cv.COLOR_BGR2GRAY) # convert from BGR to GRAY
yao_smooth = cv.GaussianBlur(yao, (3, 3), 0) # use Gaussian filter to smooth the image
Gx = cv.Sobel(yao, cv.CV_16SC1, 1, 0)
Gy = cv.Sobel(yao, cv.CV_16SC1, 0, 1)
Edge = cv.Canny(Gx, Gy, 50, 100) # perform Canny edge detection
plt.subplot(236)
plt.imshow(Edge, cmap = 'gray')
plt.title('Canny Edge')
plt.xticks([])
plt.yticks([])






