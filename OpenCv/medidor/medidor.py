import numpy as np
import cv2

cap = cv2.VideoCapture(0)

while True:
    _, frame = cap.read()
    
    #frame = frame[200:500, 0:400]
    
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    #fgmask = fgbg.apply(gray)
    
    retval, thresh = cv2.threshold(gray, 100, 255, cv2.THRESH_BINARY)
    
    kernel = np.ones((5,5),np.uint8)
    
    dilation = cv2.dilate(thresh,kernel,iterations = 1)  
    
    contours,_ = cv2.findContours(dilation,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    
    for cnt in contours:
        (x,y,w,h) = cv2.boundingRect(cnt)       
        area = cv2.contourArea(cnt)
        
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)
        
        cv2.putText(frame, "w: " + str(int(w)), (x, y+h+15), cv2.FONT_HERSHEY_SIMPLEX, 0.4, (0, 255, 255),1)
        cv2.putText(frame, "h: " + str(int(h)), (x+w+15, y+h+15), cv2.FONT_HERSHEY_SIMPLEX, 0.4, (0, 255, 255),1)
        
        if 0xFF == ord('q'):
            break
        
    
    cv2.imshow("frame", frame)                              # mostra o frame
    cv2.imshow("dilation", dilation)

    if cv2.waitKey(30) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()