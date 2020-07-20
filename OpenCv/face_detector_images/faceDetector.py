import cv2
import numpy as np

img = cv2.imread('rosto.jpg')

#img = cv2.resize(img, (325, 235))

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

while True:

    cv2.imshow('gray', gray)
    cv2.imshow('imagem', img)

    faces = face_cascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=4,
        minSize=(40, 40),
        flags=cv2.CASCADE_SCALE_IMAGE
    )
    
    for (x, y, w, h) in faces:
        
        cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)
        
        # * recorte do rosto
        roi_gray = gray[y:y+h, x:x+w]
        
        eyes = eye_cascade.detectMultiScale(
            roi_gray,
            scaleFactor=1.1,
            minNeighbors=3,
            minSize=(1, 1),
            flags=cv2.CASCADE_SCALE_IMAGE
        )
        for (x, y, w, h) in eyes:
            cv2.rectangle(img, (x, y), (x+w, y+h), (0, 0, 255), 2)
        
    if cv2.waitKey(30) & 0xFF == ord('q'):
        break