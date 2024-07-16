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