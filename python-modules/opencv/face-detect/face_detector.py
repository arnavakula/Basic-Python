import cv2

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

img = cv2.imread('news.jpg')
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

faces = face_cascade.detectMultiScale(gray_img, scaleFactor = 1.1, minNeighbors = 5)

for x, y, w, h in faces:
    gray_img = cv2.rectangle(img, (x, y), (x+w, y+h), (0, 0, 255), 3)


rgray_img = cv2.resize(gray_img, (int(gray_img.shape[1]/3), int(gray_img.shape[0]/3)))

cv2.imshow('face', gray_img)
cv2.waitKey(5000)