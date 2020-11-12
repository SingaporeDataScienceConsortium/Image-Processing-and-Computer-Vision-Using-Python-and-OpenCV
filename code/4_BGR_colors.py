# The code is shared on SDSC Github

import numpy as np
from matplotlib import pyplot as plt

plt.subplot(3, 3, 1) # create panel (3 rows and 3 columns) and locate to the first sub-figure
RGB = np.zeros([50,50,3], dtype = 'uint8')
RGB[:,:,0] = 0 # define the intensity (0-255) in channel 1 - Red
RGB[:,:,1] = 0 # define the intensity (0-255) in channel 2 - Green
RGB[:,:,2] = 0 # define the intensity (0-255) in channel 3 - Blue
plt.imshow(RGB) # display the merged color
plt.title('R G B = 0 0 0') # title
plt.xticks([]) # remove x axis
plt.yticks([]) # remove y axis

plt.subplot(3, 3, 2)
RGB = np.zeros([50,50,3], dtype = 'uint8')
RGB[:,:,0] = 128
RGB[:,:,1] = 0
RGB[:,:,2] = 0
plt.imshow(RGB)
plt.title('R G B = 128 0 0')
plt.xticks([])
plt.yticks([])

plt.subplot(3, 3, 3)
RGB = np.zeros([50,50,3], dtype = 'uint8')
RGB[:,:,0] = 255
RGB[:,:,1] = 0
RGB[:,:,2] = 0
plt.imshow(RGB)
plt.title('R G B = 255 0 0')
plt.xticks([])
plt.yticks([])

plt.subplot(3, 3, 4)
RGB = np.zeros([50,50,3], dtype = 'uint8')
RGB[:,:,0] = 0
RGB[:,:,1] = 128
RGB[:,:,2] = 128
plt.imshow(RGB)
plt.title('R G B = 0 128 128')
plt.xticks([])
plt.yticks([])

plt.subplot(3, 3, 5)
RGB = np.zeros([50,50,3], dtype = 'uint8')
RGB[:,:,0] = 128
RGB[:,:,1] = 128
RGB[:,:,2] = 128
plt.imshow(RGB)
plt.title('R G B = 128 128 128')
plt.xticks([])
plt.yticks([])

plt.subplot(3, 3, 6)
RGB = np.zeros([50,50,3], dtype = 'uint8')
RGB[:,:,0] = 255
RGB[:,:,1] = 128
RGB[:,:,2] = 128
plt.imshow(RGB)
plt.title('R G B = 255 128 128')
plt.xticks([])
plt.yticks([])

plt.subplot(3, 3, 7)
RGB = np.zeros([50,50,3], dtype = 'uint8')
RGB[:,:,0] = 0
RGB[:,:,1] = 255
RGB[:,:,2] = 255
plt.imshow(RGB)
plt.title('R G B = 0 255 255')
plt.xticks([])
plt.yticks([])

plt.subplot(3, 3, 8)
RGB = np.zeros([50,50,3], dtype = 'uint8')
RGB[:,:,0] = 128
RGB[:,:,1] = 255
RGB[:,:,2] = 255
plt.imshow(RGB)
plt.title('R G B = 128 255 255')
plt.xticks([])
plt.yticks([])

plt.subplot(3, 3, 9)
RGB = np.zeros([50,50,3], dtype = 'uint8')
RGB[:,:,0] = 255
RGB[:,:,1] = 255
RGB[:,:,2] = 255
plt.imshow(RGB)
plt.title('R G B = 255 255 255')
plt.xticks([])
plt.yticks([])

