# 행렬 크기 및 위상 연산 

# cv2.magnitude --- 크기 계산
# cv2.phase     --- 방향 (각도) 계산

# cv2.cartToPolar --- 극 좌표로 변환
# cv2.polarToCart --- 직교 좌표로 변환

import cv2
import numpy as np

x = np.array( [1,2,3,5,10], np.float32)
y = np.array( [2,5,7,2,9] ).astype(np.float32)

magnitude = cv2.magnitude(x,y)
phase = cv2.phase(x,y)

print(magnitude)
print(phase)

p_magnitude, p_phase = cv2.cartToPolar(x, y)

print(p_magnitude)
print(p_phase)

x2, y2 = cv2.polarToCart(p_magnitude,p_phase) # 원래의 값으로 돌아오긴 하지만 약간의 오차가 존재 (2 => 1.9999..)

print(x2)
print(y2)



