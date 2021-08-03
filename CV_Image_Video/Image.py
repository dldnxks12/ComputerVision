# imread  : 이미지 불러오기 (numpy arr)

import cv2

def print_matInfo(name, Image): # Matrix data type

    # U : unsigned
    # S : Signed
    # F : Float
    if Image.dtype == 'uint8':
        mat_type = 'CV_8U' 
    elif Image.dtype == 'int8':
        mat_type = 'CV_8S'
    elif Image.dtype == 'uint16':
        mat_type = 'CV_16U'
    elif Image.dtype == 'int16':
        mat_type = 'CV_16S'
    elif Image.dtype == 'float32':
        mat_type = 'CV_32F'
    elif Image.dtype == 'float64':
        mat_type = 'CV_64F'

    if Image.ndim == 3:
        nchannel = 3
    else:
        nchannel = 1

    print("%12s : depth(%s), channels(%s) --> mat_type(%sC%d)" % (name, Image.dtype, nchannel, mat_type, nchannel))

title1 = 'gray'
title2 = 'color'
gray = cv2.imread("OpenCV/CV_Image_Video/1.jpg", cv2.IMREAD_GRAYSCALE)
color = cv2.imread("OpenCV/CV_Image_Video/1.jpg", cv2.IMREAD_COLOR)


if gray is None or color is None:
    raise Exception("영상 파일 읽기 에러")

print("행렬 좌표 (100,100) 의 화소값 ")

print("%s %s" % (title1, gray[100,100]))
print("%s %s\n" % (title2, color[100,100]))

print_matInfo(title1, gray)
print_matInfo(title2, color)

cv2.imshow(title1, gray)
cv2.imshow(title2, color)

cv2.waitKey(0)
cv2.destroyAllWindows()

'''
행렬 좌표 (100,100) 의 화소값 
gray 193 -----> 1 channel value
color [253 200 157] ----> 3 channel value 

         gray : depth(uint8), channels(1) --> mat_type(CV_8UC1)
        color : depth(uint8), channels(3) --> mat_type(CV_8UC3)

'''