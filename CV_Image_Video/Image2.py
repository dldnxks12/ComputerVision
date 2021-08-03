# imwrite : 이미지 저장하기 (numpy arr)

import cv2

# imread로 이미지 불러오기 -> Matrix -> imwrite로 이미지 내보내기

image = cv2.imread("OpenCV\CV_Image_Video\gy.jpg", cv2.IMREAD_COLOR)
if image is None:
    raise Exception("이미지 불러오기 에러")

param_jpg = [cv2.IMWRITE_JPEG_QUALITY, 10]   # JPEG 화질
param_png = [cv2.IMWRITE_PNG_COMPRESSION, 9] # PNG 압축

cv2.imwrite("OpenCV/CV_Image_Video/test1.jpg", image) # default로 95로 설정된 화질의 이미지로 저장
cv2.imwrite("OpenCV/CV_Image_Video/test2.jpg", image, param_jpg)
cv2.imwrite("OpenCV/CV_Image_Video/test3.png", image, param_png) # 압축된 PNG 이미지 
cv2.imwrite("OpenCV/CV_Image_Video/test4.bmp", image) # bmp file -> raw file 처럼 용량이 매우 큼

print("이미지 저장 완료")