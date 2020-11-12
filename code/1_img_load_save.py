# The code is shared on SDSC Github

import cv2 as cv # import OpenCV
import os
from matplotlib import pyplot as plt # function for display option 2

# create a folder to save results
if not os.path.exists('results'):
    os.makedirs('results')

fruit = cv.imread('../data/fruits.jpg') # read image
fruit_orange = fruit[150 :240, 160:260, :] # define and crop the region of orange


# display option 1
cv.imshow("Fruits", fruit) # show the original image
cv.imshow("Orange", fruit_orange) # show the cropped image
cv.waitKey(0) # wait for any key press
cv.destroyAllWindows() # close the window
cv.imwrite('results/fruits_cv.jpg', fruit_orange) # save the image of orange


# display option 2
plt.subplot(1, 2, 1) # create panel (1 row and 2 columns) and locate to the first sub-figure

# convert the image from BGR to RGB if we want to use matplotlib to display the figure
fruit = cv.cvtColor(fruit, cv.COLOR_BGR2RGB)

plt.imshow(fruit) # show the original image
plt.title('Fruits') # title
plt.xticks([]) # remove x axis
plt.yticks([]) # remove y axis

plt.subplot(1, 2, 2) # locate to the second sub-figure
fruit_orange = cv.cvtColor(fruit_orange, cv.COLOR_BGR2RGB)
plt.imshow(fruit_orange) # show the cropped image
plt.title('Orange')
plt.xticks([])
plt.yticks([])

plt.savefig('results/fruits_plt.jpg') # save the figure



