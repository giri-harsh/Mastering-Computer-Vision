import os
import numpy as np
import cv2

img_path = r"C:\Work\Programing Language\Python\Libraries\OpenCV\data\img.png"
img = cv2.imread(img_path)

def draw(event, x, y, flags, params):
    if event == cv2.EVENT_LBUTTONDOWN:
        cv2.circle(img, center=(x, y), radius=20, color=(0,0,255), thickness=-1)

cv2.namedWindow('window')
cv2.setMouseCallback('window', draw)

while True:
    cv2.imshow('window', img)

    key = cv2.waitKey(1) & 0xFF

    if key == ord("x"):
        break

    if key == ord("s"):
        cv2.imwrite('img_modified.png', img)
        print("Image saved")

cv2.destroyAllWindows()
