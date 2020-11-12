# The code is shared on SDSC Github

import cv2 as cv

yao = cv.imread("../data/yao.jpg") # read image of a single face
yao_gray = cv.cvtColor(yao, cv.COLOR_BGR2GRAY) # convert from BGR to GRAY

# load the classifier for face detection
face_cascade = cv.CascadeClassifier('../data/haarcascades/haarcascade_frontalface_default.xml')

eye_cascade = cv.CascadeClassifier('../data/haarcascades/haarcascade_eye.xml') # load the classifier for eye detection

faces = face_cascade.detectMultiScale(yao_gray, 1.3, 5) # detect the face

for (face_x,face_y,width,height) in faces: # go through each face
    cv.rectangle(yao,(face_x,face_y),(face_x+width,face_y+height),(255,0,0),2) # draw a box enclosing the face
    roi_gray = yao_gray[face_y:face_y+height, face_x:face_x+width] # crop the region of face in the gray image
    eyes = eye_cascade.detectMultiScale(roi_gray) # detect eyes in the cropped region
    for (eye_x,eye_y,ewidth,eheight) in eyes: # go through each eye
        cv.rectangle(yao,(eye_x+face_x,eye_y+face_y),(eye_x+ewidth+face_x,eye_y+eheight+face_y),(0,255,0),2)
        # draw a box enclosing the eye


cv.imshow('One face',yao)

nba_faces = cv.imread("../data/nba_faces.jpg") # read image of a multiple faces
nba_faces_gray = cv.cvtColor(nba_faces, cv.COLOR_BGR2GRAY)

face_cascade = cv.CascadeClassifier('../data/haarcascades/haarcascade_frontalface_default.xml')
eye_cascade = cv.CascadeClassifier('../data/haarcascades/haarcascade_eye.xml')

faces = face_cascade.detectMultiScale(nba_faces_gray, 1.3, 5)

for (face_x,face_y,width,height) in faces:
    cv.rectangle(nba_faces,(face_x,face_y),(face_x+width,face_y+height),(255,0,0),2)
    roi_gray = nba_faces_gray[face_y:face_y+height, face_x:face_x+width]
    eyes = eye_cascade.detectMultiScale(roi_gray)
    for (eye_x,eye_y,ewidth,eheight) in eyes:
        cv.rectangle(nba_faces,(eye_x+face_x,eye_y+face_y),(eye_x+ewidth+face_x,eye_y+eheight+face_y),(0,255,0),2)

cv.imshow('Multiple faces',nba_faces)

cv.waitKey(0) # wait for any key press
cv.destroyAllWindows() # close all windows











