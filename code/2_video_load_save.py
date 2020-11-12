# The code is shared on SDSC Github

import cv2 as cv
import os

# create a folder to save results
if not os.path.exists('results'):
    os.makedirs('results')

video = cv.VideoCapture('../data/fire.mp4') # read the original video
video_crop = cv.VideoCapture('../data/fire.mp4') # read the original video; later crop from this video
Nframes = int(video.get(cv.CAP_PROP_FRAME_COUNT)) # get the number of frames

for i in range(Nframes): # go through each frame of the movie
    ret, frame = video.read() # read each frame
    cv.imshow('Fire',frame) # display the frame
    cv.waitKey(1) # wait for 1ms
video.release() # close the opened file
cv.destroyAllWindows() # close the window after the movie

fourcc = cv.VideoWriter_fourcc(*'mp4v') # specify the video code
video_out = cv.VideoWriter('results/fire_crop.mp4',fourcc, 30.0, (600, 300)) # initialize a video object


for i in range(Nframes):
    ret, frame = video_crop.read() # read each frame
    frame = frame[300:600, 300:900, :] # crop this frame
    cv.imshow('Fire Crop',frame) # show the cropped frame
    cv.waitKey(1) # wait for 1ms
    video_out.write(frame) # write into the movie


### start from the 100th frame
#s = 100
#video_crop.set(1, s)
#for i in range(s, Nframes):
#    print(i)
#    ret, frame = video_crop.read() # read each frame
#    frame = frame[300:600, 300:900, :] # crop this frame
#    cv.imshow('Fire Crop',frame) # show the cropped frame
#    cv.waitKey(1) # wait for 1ms
#    video_out.write(frame) # write into the movie
### start from the 100th frame


# release all video objects
video.release()
video_crop.release()
video_out.release()

cv.destroyAllWindows() # close all windows


