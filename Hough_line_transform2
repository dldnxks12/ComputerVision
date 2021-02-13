import cv2
import numpy as np

src = cv2.imread('kong.jpg')
img = src.copy()

kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3,3),(-1,-1))  # 모폴로지 연산을 위한 구조 요소 정의 -> 사각형 구조 요소

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
_, binary = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY) # Gray Color 로 변환한 이미지 이진화 진행

morp = cv2.dilate(binary, kernel)
morp = cv2.erode (morp, kernel,iterations = 5)
morp = cv2.dilate(morp, kernel,iterations = 2)

canny = cv2.Canny(morp, 0, 0, apertureSize = 3, L2gradient = True)

cv2.imshow('kong_morp', morp)

lines = cv2.HoughLines(canny, 1, np.pi/180, 140, srn = 50, stn = 10, min_theta = 0, max_theta = np.pi/2)

for i in lines:
    rho, theta = i[0][0], i[0][1]
    a, b = np.cos(theta), np.sin(theta)
    x0, y0 = a*rho, b*rho
    
    scale = img.shape[0]+img.shape[1] # 대각선 길이 근사치 (절대값)
    
    x1 = int(x0 + scale*-b) 
    y1 = int(y0 + scale* a)
    x2 = int(x0 - scale*-b) 
    y2 = int(y0 - scale* a)
    
    cv2.line(img,(x1,y1),(x2,y2),(0,255,255), 2)
    cv2.circle(img, (x0,y0), 3, (255,0,0), 5, cv2.FILLED)

cv2.imshow("img",img)    
cv2.waitKey()
cv2.destroyAllWindows()
