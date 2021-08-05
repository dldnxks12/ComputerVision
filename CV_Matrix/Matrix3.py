# 산술 연산 함수 

# OpenCV의 배열에 대한 사칙 연산은 모두 element-wise / per-element 연산 (같은 위치에 있는 원소끼리 연산)
# 사칙 원산에 대한 인자는 모두 numpy array만 가능 (list, tuple x)

# cv2.saturate -> 0 이하 0으로, 255이상 255로 

# cv2.add()
# cv2.subtract()
# cv2.multiply
# cv2.divide()
# cv2.addWeighted() --- 두 배열의 각 원소에 가중치를 곱한 후 원소 간 합

# 곱셈과 나눗셈 과정에서 행렬의 자료형을 벗어나는 경우가 있으므로 형 변환에 유의한다.

import cv2
import numpy as np



m1 = np.full((3,6), 10 , np.uint8)
m2 = np.full((3,6), 50 , np.uint8)

m_mask = np.zeros(m1.shape, np.uint8) # mask
m_mask[ : , 3:] = 1 # 모든 행의 3 ~ 6행까지 masking 제외

m_add1 = cv2.add(m1, m2)
m_add2 = cv2.add(m1,m2, mask = m_mask)

print(m_add1)
print(m_add2)

m_div1 = cv2.divide(m1,m2)

m1 = m1.astype(np.float32)
m2 = np.float32(m2)

m_div2 = cv2.divide(m1,m2)

print(m_div1)
print(m_div2)



