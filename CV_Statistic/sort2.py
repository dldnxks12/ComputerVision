# cv2.sortIdx() 이용

# 5개 쌍의 시작좌표, 종료 좌표를 임의로 생성한다.
# 이 좌표들로 사각형을 구성하여 넓이를 구한다.
# 사각형을 넓이순으로 정렬하여 출력한다.

import cv2
import numpy as np

def print_rects(rects):
    print("-" * 46)
    print("사각형 원소\t\t사각형 정보\t사각형 크기")
    print("-" * 46)

    for i, (x, y, width, height, area) in enumerate(rects):
        print(f"rects{i} = [({x} , {y})  [{width}, {height}] and Area : {area}")

rands = np.zeros((5,5), np.uint16) # 5x5 random array

# cv2.randn(dst,mean,stddev) : random한 정규분포 생성
StartPos = cv2.randn(rands[:, :2], 100, 50) # 0열, 1열 random 생성
EndPos = cv2.randn(rands[:, 2:-1], 300, 50) # 2열, 3열 random 생성

sizes = cv2.absdiff(StartPos, EndPos) # |StartPos - EndPos|
areas = sizes[:,0] * sizes[:,1]
rects = rands.copy()

rects[:, 2:-1] = sizes
rects[:,-1] = areas

print(rects)

idx = cv2.sortIdx(areas, cv2.SORT_EVERY_COLUMN).flatten()

print_rects(rects[[idx])
