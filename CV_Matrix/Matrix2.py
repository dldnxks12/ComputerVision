'''
# Matrix의 Channel 처리 

Color Img 는 R G B 3 개의 2차원 Matrix를 합쳐 놓은 것이라 생각할 수 있다.

각 채널의 3개의 같은 위치의 Pixel로 하나의 Color Image Pixel을 표현한다. 
'''

# cv2.split() : Channel Split
# cv2.merge() : Channel Merge

# 1. 단일 채널 행렬 3개를 만들고, 3개의 채널을 합쳐 하나의 다채널 행렬로 만들기
# 2. 다시 단일 채널로 나누기

import cv2
import numpy as np


ch0 = np.zeros((200,400), np.uint8) + 10
ch1 = np.ones((200,400), np.uint8)*50
ch2 = np.full((200,400), 100, np.uint8)

list_bgr = [ch0, ch1, ch2]

image = cv2.merge(list_bgr)

cv2.imshow("ch0",ch0)
cv2.imshow("ch1",ch1)
cv2.imshow("ch2",ch2)
cv2.imshow("image",image)

ch3, ch4, ch5 = cv2.split(image)

cv2.imshow("ch3",ch3)
cv2.imshow("ch4",ch4)
cv2.imshow("ch5",ch5)

cv2.waitKey(0)
cv2.destroyAllWindows()



