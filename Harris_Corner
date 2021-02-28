import numpy as np
import cv2

img = cv2.imread("chess.jpg")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
gray = np.float32(gray)

dst = cv2.cornerHarris(gray, 2, 3, 0.04)
dst = cv2.dilate(dst, None)  # 찾아낸 feature들 확대

cv2.imshow("Corner", dst)

img[dst > 0.01*dst.max()] = [0,0,255] # 3개 채널 RGB색 모두 0,0,255 로 만듦

cv2.imshow("img",img)

cv2.waitKey()
cv2.destroyAllWindows()
