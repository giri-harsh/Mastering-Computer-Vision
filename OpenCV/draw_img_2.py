import cv2
import numpy as np

img = np.zeros((512,512,3))
drawing = False
ix = -1
iy = -1
def draw(event , x,y,flags,param):
    global drawing , ix,iy
    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        ix = x
        iy = y
        print("1")
    if event == cv2.EVENT_MOUSEMOVE:
        if drawing == True:
            cv2.rectangle(img , pt1=(ix,iy),pt2=(x,y),color=(256,0,0),thickness=-3)
            print("2")
    if event ==  cv2.EVENT_LBUTTONUP:
        drawing = False
        cv2.rectangle(img , pt1=(ix,iy),pt2=(x,y),color=(256,0,0),thickness=-3)
        print("3")

cv2.namedWindow(winname='img')
cv2.setMouseCallback('img',draw)
while True:
    cv2.imshow('img',img)
    if cv2.waitKey(1) & 0xFF == ord('x'):
        break
cv2.destroyAllWindows()