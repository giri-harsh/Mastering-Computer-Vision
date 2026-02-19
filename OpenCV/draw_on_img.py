import cv2
import numpy as np 
img = np.zeros((512,512,3)) 
ix = -1
iy= -1

def draw(event , x ,y ,flags, param):
    global ix ,iy
    ix,iy = x,y

    if event == cv2.EVENT_LBUTTONDOWN : 

        cv2.circle(img,center=(x,y),radius=8,color= (0,256,256),thickness=3)
        print("l bytton")
    if event == cv2.EVENT_RBUTTONDOWN :
        cv2.rectangle(img , pt1=(ix,iy),pt2=(x,y),color=(256,0,0),thickness=3)
        print("r button")


cv2.namedWindow(winname='window')
cv2.setMouseCallback('window',draw)
while True:
    cv2.imshow("window",img)
    if cv2.waitKey(1) & 0xFF == ord('x'):
        break
cv2.destroyAllWindows() 
    
