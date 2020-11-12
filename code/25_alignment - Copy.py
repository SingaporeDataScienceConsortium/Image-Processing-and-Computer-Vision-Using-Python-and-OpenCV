# The code is shared on SDSC Github

import cv2 as cv
import numpy as np

max_features = 500 # maximum features to consider
match_threshold = 0.15 # only consider 15% of the matched points

ref = cv.imread('../data/board_ref.jpg') # read reference image

toAlign = cv.imread('../data/board_toAlign.jpg') # read image to align

#toAlignGray = cv.cvtColor(toAlign, cv.COLOR_BGR2GRAY) # convert from BGR to GRAY
#refGray = cv.cvtColor(ref, cv.COLOR_BGR2GRAY)

toAlignGray = toAlign
refGray = ref

orb = cv.ORB_create(max_features) # Initiate ORB detector

# find the keypoints and descriptors for the image to align
keyPts_toAlign, descrip_toAlign = orb.detectAndCompute(toAlignGray, None,1,1,1)

# find the keypoints and descriptors for the reference image
keyPts_ref, descrip_ref = orb.detectAndCompute(refGray, None)

matcher = cv.DescriptorMatcher_create(cv.DESCRIPTOR_MATCHER_BRUTEFORCE_HAMMING) # initialize a descriptor matcher
matches = matcher.match(descrip_toAlign, descrip_ref) # match two images

matches.sort(key=lambda x: x.distance, reverse=False) # sort the matched points (from good to bad)

# only consider 15% of the matched points
numGoodMatches = int(len(matches) * match_threshold)
matches = matches[0:numGoodMatches]

#imMatches = cv.drawMatches(toAlign, keyPts_toAlign, ref, keyPts_ref, matches, None) # draw key point correspondence
imMatches = cv.drawMatches(toAlign, keyPts_toAlign, ref, keyPts_ref, matches, outImg=None) # draw key point correspondence
cv.imshow('Matches', cv.resize(imMatches, (616*2, 410, )))
cv.waitKey(3000)
cv.destroyAllWindows()

# initialize paired points with zero for alignment
Pts_toAlign = np.zeros((len(matches), 2), dtype=np.float32)
Pts_ref = np.zeros((len(matches), 2), dtype=np.float32)

for i, match in enumerate(matches): # assign coordinates to the paired points
      Pts_toAlign[i, :] = keyPts_toAlign[match.queryIdx].pt
      Pts_ref[i, :] = keyPts_ref[match.trainIdx].pt

T_matrix, mask = cv.findHomography(Pts_toAlign, Pts_ref, cv.RANSAC) # determine the Homography
#T_matrix = cv.findHomography(Pts_toAlign, Pts_ref, cv.RANSAC) # determine the Homography

h, w, channels = ref.shape
Img_Aligned = cv.warpPerspective(toAlign, T_matrix, (w, h)) # perform perspective transformation

cv.namedWindow('Aligned Image', cv.WINDOW_NORMAL)
for i in range(20):
      cv.imshow('Aligned Image', ref)
      cv.waitKey(100)
      cv.imshow('Aligned Image', Img_Aligned)
      cv.waitKey(100)

cv.waitKey() # wait for any key press
cv.destroyAllWindows() # close all windows


