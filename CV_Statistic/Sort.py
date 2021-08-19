# 행렬 원소 정렬 : cv2.sort(), np.sort()
# 정렬 Index 반환 : cv2.sortIdx(), np.argsort()
import cv2
import numpy as np

# 0 ~ 100 까지 숫자 15개 random pick and reshape 3 x 5 matrix
matrix = np.random.randint(0,100,15).reshape(3,5)
print(matrix.shape)

# with cv2
# sort : row , ascending
sort1 = cv2.sort(matrix, cv2.SORT_EVERY_ROW)
# sort : row , descending
sort2 = cv2.sort(matrix, cv2.SORT_EVERY_ROW+cv2.SORT_DESCENDING)
# sort : col , ascending
sort3 = cv2.sort(matrix, cv2.SORT_EVERY_COLUMN)
# sort : col , descending
sort4 = cv2.sort(matrix, cv2.SORT_EVERY_COLUMN+cv2.SORT_DESCENDING)

# with Numpy
# sort : x axis
sort5 = np.sort(matrix, axis = 1)
# sort : y axis
sort6 = np.sort(matrix, axis = 0)

# return sort Index - 행렬의 원소를 직접 정렬하지 않고, 정렬된 원소의 원 Index를 반환한다.

# cv2
Idx_sort1 = cv2.sortIdx(matrix, cv2.SORT_EVERY_ROW)
'''
[[2 0 1 4 3]
 [4 1 2 3 0]
 [1 0 3 4 2]]
'''
Idx_sort2 = cv2.sortIdx(matrix, cv2.SORT_EVERY_COLUMN)

# numpy
Idx_sort3 = np.argsort(matrix, axis = 0) # y axis
