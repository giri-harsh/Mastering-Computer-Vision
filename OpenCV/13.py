import numpy
import os
import cv2


img = cv2.imread(r'C:\Work\Programing Language\Python\Libraries\OpenCV\data\image.png')
flag = False
ix = -1
iy = -1

def crop (event,x,y,flags, params):
    global flag , ix, iy
    if event ==1 :
        flag = True
        ix = x
        iy = y 
        
        print("1 done")
    # elif event == 0:
    #     if flag == True:
    #         cv2.rectangle(img,pt1=(ix , iy),pt2 = (x,y),color=(0,255,255),thickness=-1)
    #         print ("2 done")
    elif event == 4:
        fx = x
        fy = y 

        flag == False
        cv2.rectangle(img,pt1=(ix , iy),pt2 = (x,y),color=(0,0,0),thickness=1)
        cropped = img[iy : fy , ix : fx]
        cv2.imshow('new win',cropped) 
        cv2.waitKey(0)
        
cv2.namedWindow(winname='window')
cv2.setMouseCallback('window',crop)


while True:
    cv2.imshow('window',img)
    if cv2.waitKey(1) & 0xFF == ord('x'):
        break
cv2.destroyAllWindows()