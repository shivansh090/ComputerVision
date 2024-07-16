# import cv2

# img = cv2.imread("./Resources/tilted.jpeg")

# img=cv2.resize(img,0.5)
# cv2.imshow("Image",img)
# cv2.waitKey(0)
import cv2
import numpy as np

imgorig = cv2.imread("Resources/tilted.jpeg")
img=cv2.resize(imgorig, (0,0), None, 0.2, 0.2)
width,height = 500,700
pts1 = np.float32([[445,417],[2365,773],[205,3473],[2905,3201]])
pts2 = np.float32([[0,0],[width,0],[0,height],[width,height]])
matrix = cv2.getPerspectiveTransform(pts1,pts2)
imgOutput = cv2.warpPerspective(imgorig,matrix,(width,height))


cv2.imshow("Image",img)
cv2.imshow("Output",imgOutput)

cv2.waitKey(0)