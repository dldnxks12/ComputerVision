
# cv2.min
# cv2.max
# cv2.minMaxLoc() - 입력 배열에서 최대, 최소, 그리고 그 위치를 반환

import cv2
import numpy as np

data = [ 10, 200, 5, 7,9, 15, 35, 60, 80, 180, 100, 2, 55, 27, 70]

m1 = np.reshape(data, (3,5))
m2 = np.full((3,5), 50)

m_min = cv2.min(m1, 30)  # 각 원소와 30을 비교해서 작은 값으로 return 
m_max = cv2.max(m1, m2)

print("min",m_min)
print("max",m_max)

'''
min [[10 30  5  7  9]
 [15 30 30 30 30]
 [30  2 30 27 30]]
max [[ 50 200  50  50  50]
 [ 50  50  60  80 180]
 [100  50  55  50  70]]

'''

min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(m1)

print(min_val, max_val, min_loc, max_loc) # 2.0 200.0 (1, 2) (1, 0)