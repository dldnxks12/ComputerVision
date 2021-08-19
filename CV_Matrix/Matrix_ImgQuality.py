# 화소의 최대, 최소값 간 차이가 적을 때, 즉 사진 내의 객체가 구별이 잘 안되는 경우 최대 255, 최소 0으로 조정하여 화질 개선하는 방법


import numpy as np
import cv2

image = cv2.imread("OpenCV/CV_Matrix/3.jpg", cv2.IMREAD_GRAYSCALE)

if image is None:
    raise Exception("error")

cv2.imshow("before", image)

min_val, max_val, _ , _ = cv2.minMaxLoc(image) # Min, Max Value

ratio = 255/ (max_val - min_val)

dst = np.round((image - min_val)*ratio).astype(np.uint8)


cv2.imshow("before", image)
cv2.imshow("After", dst)

cv2.waitKey(0)
cv2.destroyAllWindows()

