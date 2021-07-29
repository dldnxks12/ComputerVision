import numpy as np
import cv2

image = np.zeros((200,400),np.uint8) # 200x400 크기 matrix 생성
image[:] = 200 # image.fill(200)로도 사용가능 -> 200x400 matrix를 200의 값으로

title1, title2 = 'Pos1', 'Pos2'

cv2.namedWindow(title1, cv2.WINDOW_AUTOSIZE) # image matrix에 맞게 window 생성 , 이미지 크기 변경 불가
cv2.namedWindow(title2, cv2.WINDOW_NORMAL)  # 이미지 크기 변경 가능

cv2.moveWindow(title1, 150,150) # 모니터 기준 좌측 상단이 0,0
cv2.moveWindow(title2, 400,50)

cv2.imshow(title1, image) # title1 이라는 이름 없을 시 , default name응로 생성
cv2.imshow(title2, image)

cv2.resizeWindow(title1, 400,300)
cv2.resizeWindow(title2, 400,300)

cv2.waitKey(0)
cv2.destroyAllWindows()
