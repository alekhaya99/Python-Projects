from cv2 import cv2
import numpy as np
import pyautogui

record=cv2.VideoCapture(0)
low_green = np.array([25, 52, 72])
high_green = np.array([102, 255, 255])
original_y=0
while True:
    # Retreival and frame
    ret,frame=record.read()
    #in order to convert the frame the hue saturation frame
    hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    #Specifying the mask range value
    mask=cv2.inRange(hsv,low_green,high_green)

    contours,hierarchy=cv2.findContours(mask,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)

    for c in contours:
        Area=cv2.contourArea(c)
        if Area>500:
            x_pos,y_pos,width,height=cv2.boundingRect(c)
            cv2.rectangle(frame,(x_pos,y_pos),(x_pos+width,y_pos+height),(0,255,0),3)
            if y_pos<original_y:
                pyautogui.press('space')
                                      
            original_y=y_pos
            # print(Area)
            # cv2.drawContours(frame,c,-1,(0,255,0),3)

    
    cv2.imshow('frame',frame)
    # cv2.imshow('mask',mask)
    # If some body presses the key e, it will break from the loop
    if cv2.waitKey(10)==ord('e'):
        break

record.release()
cv2.destroyAllWindows() 