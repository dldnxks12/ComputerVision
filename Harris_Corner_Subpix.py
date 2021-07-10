import numpy as np
import cv2

img = cv2.imread("chess.jpg")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
gray = np.float32(gray)

dst = cv2.cornerHarris(gray, 2, 3, 0.04)
dst = cv2.dilate(dst, None)  # 찾아낸 feature들 확대

cv2.imshow("Corner", dst)

ret, dst = cv2.threshold(dst, 0.01*dst.max(), 255, 0)
dst = np.uint8(dst)

cv2.imshow("Threshold",dst)

ret, labels, stat, centroids = cv2.connectedComponentsWithStats(dst)

criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 100, 0.001)
corners = cv2.cornerSubPix(dst, np.float32(centroids), (5,5), (-1,-1), criteria)

res = np.hstack((centroids, corners))
res = np.int0(res)

print(res)

img[ res[:,1], res[:,0]] = [0,0,255]

print("img1",img)

img[ res[:,3], res[:,2]] = [0,255,0]

print("img2", img)

cv2.imshow("subpic", img)
cv2.waitKey()
cv2.destroyAllWindows()

