import cv2
import numpy as np 

circles= np.zeros((4,2),int)
count=0
def MousePoints(event,x,y,flags,params):
    global count
    if event == cv2.EVENT_LBUTTONDOWN:
        circles[count]= x,y
        count+=1
        print(circles)

width,height= 400,500
img = cv2.imread("./Resources./tilted.jpeg")
img = cv2.resize(img, (width, height))


 
cv2.imshow("IMG",img)
cv2.setMouseCallback("IMG",MousePoints)
cv2.waitKey(0)