import os
import numpy as np
import cv2

img = np.zeros((512,512,3))

def draw(event , x,y,flag,params):
    if event == 1:
        cv2.circle(img,center=(x,y),radius=20,color=(0,255,255),thickness=-1)
    if event == 2:
        cv2.circle(img,center=(x,y),radius=20,color=(0,255,0),thickness=2)
    if event == 4:
        print("Left Release")
    if event == 5:
        print("Right Release")

cv2.namedWindow('window')
cv2.setMouseCallback('window',draw)
while True:
    cv2.imshow('window',img)

    if cv2.waitKey(1) & 0xFF == ord('x'):
        break
cv2.destroyAllWindows()


