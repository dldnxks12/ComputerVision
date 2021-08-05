# Bit-wise 연산

# 원소의 비트 단위로 논리 연산을 수행한다. 

# cv2.bitwise_and
# cv2.bitwise_or
# cv2.bitwise_xor
# cv2.bitwise_not

# and or xor not은 global logic gate로써 나머지 Nand, Nor, Xnor 등을 생성하는 기본 블럭이 될 수 있다.


import numpy as np
import cv2


image1 = np.zeros((300,300), np.uint8)
image2 = image1.copy() # numpy function

h, w = image1.shape[:2]

cx, cy = w//2, h//2

cv2.circle(image1, (cx,cy), 100, 255, -1)
cv2.rectangle(image2, (0,0, cx, h), 255, -1)


cv2.imshow("image1",image1)
cv2.imshow("image2",image2)


image3 = cv2.bitwise_and(image1, image2)
image4 = cv2.bitwise_or(image1, image2)
image5 = cv2.bitwise_xor(image1, image2)
image6 = cv2.bitwise_not(image1, image2)

cv2.imshow("image3",image3)
cv2.imshow("image4",image4)
cv2.imshow("image5",image5)
cv2.imshow("image6",image6)


cv2.waitKey(0)
cv2.destroyAllWindows()
