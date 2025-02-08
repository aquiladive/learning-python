import cv2

face_cascade = cv2.CascadeClassifier(cv2.data_haarcascade+"haarcasecade_frontalface_default.xml")
eye_cascade = cv2.CascadeClassifier(cv2.data_haarcascade+"haarcascade_eye.xml")

img = cv2.imread("img.png")
grey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

faces = face_cascade.detectMultiScale(grey, scaleFactor=1.3, minNeighbors=5)

for (x,y,w,h) in faces:
    cv2.rectangle(img, (x+y), (x+w,y+h), (255,0,0), 2)

cv2.imwrite('detected.jpg', img)
cv2.imshow('Detected Faces', img)
