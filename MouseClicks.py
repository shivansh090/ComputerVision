import cv2
import numpy as np 

circles= np.zeros((4,2),int)
count=0
def MousePoints(event,x,y,flags,params):
    global count
    if event == cv2.EVENT_LBUTTONDOWN:
        circles[count]= x,y
        count=count+1

width,height= 400,500
img = cv2.imread("./Resources./tilted.jpeg")
img = cv2.resize(img, (width, height))


while True:
    if(count==4):
        pts1 = np.float32([circles[0],circles[1],circles[2],circles[3]])
        pts2 = np.float32([[0,0],[width,0],[0,height],[width,height]])
        matrix = cv2.getPerspectiveTransform(pts1,pts2)
        imgOutput = cv2.warpPerspective(img,matrix,(width,height))
        cv2.imshow("output",imgOutput)
       
    for i in circles:
        cv2.circle(img,(i),3,(0,0,255),5)

        

    cv2.imshow("IMG",img)
    cv2.setMouseCallback("IMG",MousePoints)
    cv2.waitKey(1)