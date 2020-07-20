import cv2
import numpy as np
import pickle

###    Identificadores    ###
face_cascade = cv2.CascadeClassifier('cascades/data/haarcascade_frontalface_alt2.xml')

recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read('rock_faces.yml')

labels = {}
with open("labels.pickle", "rb") as f:
    sup_labels = pickle.load(f)
    labels = {v:k for k,v in sup_labels.items()}


cap = cv2.VideoCapture(0)

while True:
    _, frame = cap.read()
    
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(
        gray,
        scaleFactor=1.5,
        minNeighbors=5,
    )
    
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
        
        roi_gray = gray[y:y+h, x:x+w]
        
        id_, conf = recognizer.predict(roi_gray)
        
        if conf >= 45:
            #print(labels[id_])
            cv2.putText(frame, labels[id_], (x, y-15), cv2.FONT_HERSHEY_SIMPLEX, 0.4, (0, 255, 255),1)
    
    
    ###    Mostrar    ###
    cv2.imshow("frame", frame)
    cv2.imshow("gray", gray)
    
    if cv2.waitKey(20) & 0xFF == ord('q'):
        break

cap.realease()
cv2.destroyAllWindows()