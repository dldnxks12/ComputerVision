# 실제 이미지를 띄워서 R G B Channel로 분리해서 보자

import cv2
import numpy as np

image = cv2.imread("C:/Users/USER/Desktop/git/OpenCV/CV_Image_Video/1.jpg", cv2.IMREAD_COLOR)

b, g, r = cv2.split(image)

cv2.imshow("blue",b)
cv2.imshow("green",g)
cv2.imshow("red",r)
cv2.imshow("image",image)

cv2.waitKey(0)
cv2.destroyAllWindows()
