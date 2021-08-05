# 지수, 로그, 제곱근 

'''

cv2.exp()  - 지수
cv2.log()  - 자연로그
cv2.sqrt() - 제곱근
cv2.pow()  - 거듭제곱


# 2차원 arr을 1차원으로 표시하는 방법

    1. ravel()
    2. flatten()
    3. arr.T

'''

import numpy as np
import cv2
from numpy.core.fromnumeric import ndim, size

v1 = np.array([1,2,3], np.float32) # 3, 행렬 (dim = 1)
v2 = np.array([ [1],[2],[3]] , np.float32) # 3 x 1 행렬 (dim = 2)  / print(ndim(v2)) == 2
v3 = np.array([ [1,2,3] ], np.float32) # 1 x 3 행령

v_exp = cv2.exp(v1)
m_exp = cv2.exp(v2)
q_exp = cv2.exp(v3)

print(v_exp.shape)
print(m_exp.shape)
print(q_exp.shape)

v_log = cv2.log(v1)
m_sqrt = cv2.sqrt(v2)
q_pow = cv2.pow(v3,3)


print(v_log.shape)
print(m_sqrt.shape)
print(q_pow.shape)

v_log = v_log.T
m_sqrt = np.ravel(m_sqrt)
q_pow = q_pow.flatten()

print(v_log.shape)
print(m_sqrt.shape)
print(q_pow.shape)

