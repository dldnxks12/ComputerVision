# 8 bit 이미지를 읽어서 16 or 32 bit 영상으로 저장해보자

import cv2
import numpy as np


image8 = cv2.imread("OpenCV/CV_Image_Video/1.jpg", cv2.IMREAD_COLOR)

if image8 is None:
    raise Exception("Error")


image16 = np.uint16(image8*(65535/255))
image32 = np.float32(image8*(1/255))

print("Image8\n %s\n" % image8[10:12, 10:13])
print("Image16\n %s\n" % image16[10:12, 10:13])
print("Image32\n %s\n" % image32[10:12, 10:13])

cv2.imshow("image8", image8)
cv2.imshow("image16", image16)
cv2.imshow("image32", image32)


cv2.waitKey(0)
cv2.destroyAllWindows()

'''
Image8
 [[[206 166 137]
  [197 152 119]
  [195 145 109]]

 [[209 172 146]
  [195 155 126]
  [193 146 114]]]

Image16
 [[[52942 42662 35209]
  [50629 39064 30583]
  [50115 37265 28013]]

 [[53713 44204 37522]
  [50115 39835 32382]
  [49601 37522 29298]]]

Image32
 [[[0.80784315 0.6509804  0.5372549 ]
  [0.77254903 0.59607846 0.46666667]
  [0.7647059  0.5686275  0.42745098]]

 [[0.81960785 0.6745098  0.57254905]
  [0.7647059  0.60784316 0.49411765]
  [0.75686276 0.57254905 0.44705883]]]
'''