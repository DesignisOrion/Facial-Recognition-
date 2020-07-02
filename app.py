# facical detection program


import numpy as np
import cv2
import matplotlib.pyplot as plt
%matplotlib inline  # sets the backend of matplotlib to the 'inline' backend:

face_image = cv2.imread('teamusa.jpg')  # reading the image
# convert to grey scale images
grey_img = cv2.cvtColor(face_image, cv2.COLOR_BGR2GRAY)

plt.figure(figsize=(20, 10))
plt.imshow(grey_img, cmap='gray')

# load training file
face_cacade = cv2.CascasdeClassifier(('haarcascade_frontalface_alt.xml'))

face_detect = face_cacade.detectMultiScale(
    grey_img, scaleFactor=1.1, minNeighbors=5)

# print the number of faces found
print 'Faces found: ', len(face_detect)
face_detect

for (x, y, w, h) in face_detect:
    cv2.rectangle(face_image, (x, y), (x+w, y+h), (0, 0, 255), 2)

plt.figure(figsize=(20, 10))
plg.imshow(cv2.cvtColor(face_image, cv2.COLOR_BGR2RGB))

'''rectangle = np.ones((720, 1280))
plt.figure(figsize=(20,10))
'''
