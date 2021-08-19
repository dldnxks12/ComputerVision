# 행렬 합 / 평균 연산

import cv2
import numpy as np

# Image Load
image = cv2.imread("./gy.jpg", cv2.IMREAD_COLOR)
# Debug code
if image is None:
    raise Exception("Error")

mask = np.zeros(image.shape[:2], np.uint8) # Image.shape[:2] = 1080 , 1440
print(image.shape)
print(mask.shape)

# ROI Setting
mask[60:160, 20:120] = 255 # 0이 아닌 어떤 값으로 써도 상관없다

# channel sum
sum_value = cv2.sumElems(image)

# channel mean
mean_value1 = cv2.mean(image)
mean_value2 = cv2.mean(image, mask) # mask를 이용해서 특정 영역에 대해서만 mean을 구할 수도 있다.

print("Sum", sum_value)
print("mean_value1",  mean_value1)
print("mean_value2", mean_value2)

# mean , stddev
mean, stddev = cv2.meanStdDev(image)
mean2, stddev2 = cv2.meanStdDev(image, mask = mask)  # mask가 255인 영역만 계산

print(f"mean: {mean} , stddev : {stddev}")
print(f"mean2: {mean2} , stddev2 : {stddev2}")

# numpy의 flatten()을 이용해서 1차원 행렬로 출력 가능
print(f"mean: {mean.flatten()} , stddev : {stddev.flatten()}")
print(f"mean2: {mean2.flatten()} , stddev2 : {stddev2.flatten()}")

cv2.imshow("GY", image)
cv2.imshow("mask", mask)

cv2.waitKey(0)
cv2.destroyAllWindows()
