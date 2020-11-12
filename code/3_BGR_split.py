# The code is shared on SDSC Github

import cv2 as cv
from matplotlib import pyplot as plt
import numpy as np

fruit = cv.imread('../data/fruits.jpg') # read the original data

# split the channels to B G R
B = fruit[:,:,0]
G = fruit[:,:,1]
R = fruit[:,:,2]

plt.subplot(2, 3, 1) # create panel (2 rows and 3 columns) and locate to the first sub-figure
plt.imshow(B, cmap = 'gray') # define the color map
plt.title('Blue Channel') # title
plt.xticks([]) # remove x axis
plt.yticks([]) # remove y axis

plt.subplot(2, 3, 2)
plt.imshow(G, cmap = 'gray')
plt.title('Green Channel')
plt.xticks([])
plt.yticks([])

plt.subplot(2, 3, 3)
plt.imshow(R, cmap = 'gray')
plt.title('Red Channel')
plt.xticks([])
plt.yticks([])

plt.subplot(2, 3, 4)
B_RGB = np.zeros(fruit.shape, dtype = 'uint8')
B_RGB[:,:,2] = B
plt.imshow(B_RGB)
plt.title('Blue RGB')
plt.xticks([])
plt.yticks([])

plt.subplot(2, 3, 5)
G_RGB = np.zeros(fruit.shape, dtype = 'uint8')
G_RGB[:,:,1] = G
plt.imshow(G_RGB)
plt.title('Green RGB')
plt.xticks([])
plt.yticks([])

plt.subplot(2, 3, 6)
R_RGB = np.zeros(fruit.shape, dtype = 'uint8')
R_RGB[:,:,0] = R
plt.imshow(R_RGB)
plt.title('Red RGB')
plt.xticks([])
plt.yticks([])

