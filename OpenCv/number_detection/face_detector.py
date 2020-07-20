# IMPORTS
import numpy as np
import cv2

def nothing(x):
    pass

# READ VIDEO
cap = cv2.VideoCapture(0)

fgbg = cv2.createBackgroundSubtractorMOG2() 

# TRACKBARS WINDOWS
cv2.namedWindow('trackbars')

cv2.createTrackbar('x','trackbars',250,800,nothing)
cv2.createTrackbar('y','trackbars',250,800,nothing)
cv2.createTrackbar('w','trackbars',600,800,nothing)
cv2.createTrackbar('h','trackbars',600,800,nothing)
cv2.createTrackbar('th','trackbars',100,255,nothing)

# LOOP
while(True):
    
    # READ FRAME
    _, frame = cap.read()

    # CATCH TRACKBARS    
    x = cv2.getTrackbarPos('x','trackbars')
    y = cv2.getTrackbarPos('y','trackbars')
    w = cv2.getTrackbarPos('w','trackbars')
    h = cv2.getTrackbarPos('h','trackbars')
    th = cv2.getTrackbarPos('th','trackbars')
    
    # CUT ROI
    roi_color = frame[y:y+h, x:x+w]
    
    # CRIAR THRESH HOLD
    gray = cv2.cvtColor(roi_color, cv2.COLOR_BGR2GRAY)
    retval, thresh = cv2.threshold(gray, th, 255, cv2.THRESH_BINARY)
    
    # KERNEL
    kernel = np.ones((5,5), np.uint8)   
    
    # EROSION
    opening = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel)
    
    dilate = cv2.dilate(opening,kernel,iterations = 2)
     
    contours, hierarchy = cv2.findContours(dilate,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
    for cnt in contours:
        
        area = cv2.contourArea(cnt)
        
        if area > 100 and area <= h * w:
            x2, y2, w2, h2 = cv2.boundingRect(cnt)
            
            cv2.rectangle(roi_color,(x2,y2),(x2+w2,y2+h2),(0,255,0),2)

    # SHOW FRAMES
    #cv2.imshow('frame',frame)
    cv2.imshow('roi', roi_color)
    #cv2.imshow("thresh", cv2.resize(thresh, (300, 300)))
    cv2.imshow("thresh", thresh)

    # WAITKEY
    if cv2.waitKey(60) & 0xFF == ord('q'):
        break

# RELEASE CAP
cap.release()

# DESTROY ALL WINDOWS
cv2.destroyAllWindows()