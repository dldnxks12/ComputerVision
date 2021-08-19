# 행렬 축소 연산 - cv2.reduce()

import cv2
import numpy as np

# np.random.randint : int 형 난수
# np.random.rand : float 형 난수
matrix = np.random.rand(3,5)*100  # 0 ~ 99 사이 float 난수

reduce_sum = cv2.reduce(matrix, dim = 0, rtype = cv2.REDUCE_SUM) # 열방향 Sum으로 축소
reduce_avg = cv2.reduce(matrix, dim = 1, rtype = cv2.REDUCE_AVG) # 행방향 Avg로 축소
reduce_max = cv2.reduce(matrix, dim = 0, rtype = cv2.REDUCE_MAX) # 열방향 Max로 축소
reduce_min = cv2.reduce(matrix, dim = 1, rtype = cv2.REDUCE_MIN) # 행방향 Min으로 축소

print(matrix)
print(reduce_sum.flatten())
print(reduce_avg.flatten())
print(reduce_max.flatten())
print(reduce_min.flatten())


