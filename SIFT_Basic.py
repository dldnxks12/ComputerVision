import cv2
import numpy as np

img = cv2.imread('gayoung.jpg') # OR random Image
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) 

sift = cv2.SIFT_create() # SIFT 객체 생성  

kp = sift.detect(gray, None) # Keypoint 찾기

img = cv2.drawKeypoints(gray, kp , img) # image에 Keypoint 표시

# cv2.imwrite('sift_keypoints.jpg', img) # image 저장

img=cv2.drawKeypoints(gray,kp,img,flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS) # Keypoint의 위치, 크기, 방향 표시

cv2.imshow("sift_keypoints.jpg", img) # image 띄우기
cv2.waitKey()
cv2.destroyAllWindows()
