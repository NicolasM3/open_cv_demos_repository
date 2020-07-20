import cv2
import numpy as np

cap = cv2.VideoCapture(0)

# * carregando pesoso para o reconhecimento
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')

while True:
    _, frame = cap.read()
    
    # * transforma a imagem para uma cor
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    #cv2.imshow("detector", gray)
    
    # * detecta 
    faces = face_cascade.detectMultiScale(gray, 1.3, 5) 
    
    # * percorre a face  
    for (x,y,w,h) in faces:
        # * desenha um retngulo no frame, da posição,
        # * na largura e atura, da cor, da espessura tal
        cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
		
        # * recorte do rosto
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = frame[y:y+h, x:x+w]
  
        # * detecta
        eyes = eye_cascade.detectMultiScale(roi_gray)
  
        # * percorre a face  
        for (ex,ey,ew,eh) in eyes:
      
            # * desenha um retngulo no frame, da posição,
            # * na largura e atura, da cor, da espessura tal
            cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)

    cv2.imshow("detector", frame)

    key = cv2.waitKey(1)
    
    if key == 27:
        break
    
cap.realease()
cap.destroyAllWindows()
