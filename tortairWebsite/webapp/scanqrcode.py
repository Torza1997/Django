import numpy as np
import cv2
import pyzbar.pyzbar as pyzbar

def Borrow_code():
    cap = cv2.VideoCapture(0)
    font = cv2.FONT_HERSHEY_PLAIN
    c = True
    while(c):
        '''ret'''
        _, frame = cap.read()
        decodebar = pyzbar.decode(frame)
        for obj in decodebar:
            Br_code = (obj.data).decode()
            cv2.putText(frame,str(Br_code),(50,50),font,3,(255,0,0),3)
            if not Br_code: 
                """"""
            else:
                c = False
        #gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        cv2.putText(frame,str("Exit Enter (q)"),(400,400),font,1,(0,0,255),1)
        cv2.imshow('frame',frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            Br_code = '0'
            break
    cap.release()
    cv2.destroyAllWindows()
    return Br_code