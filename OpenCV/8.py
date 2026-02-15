import os
import numpy as np
import cv2

img = np.zeros((512,512,3))

def draw(event , x,y,flag,params):
    if event == 1:
        print("Left Click")
    if event == 2:
        print("Right Click")
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


