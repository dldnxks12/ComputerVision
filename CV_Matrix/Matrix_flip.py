# OpenCV는 Numpy와 연동해서 배열을 생성한다.
# OpenCV는 ndarray 객체를 기반으로 입력 배열과 출력 배열을 사용한다.

# cv2.flip() : 좌우 반전
# cv2.transpose() : 입력 행렬의 전치 행렬
# cv2.repeat() : 입력 배열의 반복된 복사본으로 출력 배열만듦

import cv2

image = cv2.imread("C:/Users/USER/Desktop/git/OpenCV/CV_Image_Video/1.jpg", cv2.IMREAD_COLOR)
if image is None:
    raise Exception("error")

x_axis  = cv2.flip(image, 0)
y_axis  = cv2.flip(image, 1)
xy_axis = cv2.flip(image, -1)

rep_image = cv2.repeat(image, 1, 2)
trans_img = cv2.transpose(image)

titles = ['image','x_axis','y_axis','xy_axis','rep_image','trans_img']

for title in titles:
    cv2.imshow(title, eval(title))

# eval() 함수는 문자열을 명령어로 실행하기 때문에, 문자열을 변수로 사용한다. 

cv2.waitKey(0)