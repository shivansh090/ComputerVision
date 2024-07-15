import cv2
import numpy as np

img1=cv2.imread("./Resources/lena.png")
img2 = cv2.Canny(img1,150,200)
img2= cv2.cvtColor(img2,cv2.COLOR_GRAY2BGR)

img1=cv2.resize(img1, (0,0), None, 0.5, 0.5)
img2=cv2.resize(img2, (0,0), None, 0.5, 0.5)

imgHor = np.hstack((img1,img2))
imgVer = np.vstack((img1,img2))

cv2.imshow("Horizontal",imgHor)
cv2.imshow("Vertical",imgVer)
# cv2.imshow("ImageStack",imgStack)
cv2.waitKey(0)