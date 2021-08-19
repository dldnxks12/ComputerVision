# Histogram : 특정 데이터가 얼마나 많은지 도수 분포표를 이용하여 나타내보자

# --- Histogram 계산하기 --- #
# 1. 사용자 정의함수
# 2. OpenCV 내장함수 cv2.CalcHist()
# 3. Numpy 내장함수 np.histogram()


import numpy as np
import cv2

# --- Histogram 계산하기 --- #

def user_define_histogram(image, histsize, ranges = [0, 256]):

    hist = np.zeros((histsize, 1), np.float32) # Histogram 누적 행렬
    gap  = ranges[1] / histsize # 계급 간격

    for row in image:
        for pixel in row:
            idx = int(pixel/gap)
            hist[idx] += 1

    return hist

image = cv2.imread("./gy.jpg", cv2.IMREAD_GRAYSCALE)
if image is None:
    raise Exception("Error")

histsize = [32]
ranges = [0,256]
gap = ranges[1] / histsize[0]  # 256/32  -- 계급 크기

# user define
#hist1 = user_define_histogram(image, histsize[0], ranges)

# cv function - faster
hist2 = cv2.calcHist([image], [0], None, histsize, ranges)

# numpy function - fast
#ranges_gap = np.arange(0, ranges[1]+1, gap) # 시작 - 끝, gap 간격
#hist3 = np.histogram(image, ranges_gap)

# --- Histogram 그리기 --- #

'''
dst = cv2.normalize(src, dst, alpha, beta, type_flag)
    src: 정규화 이전의 데이터
    dst: 정규화 이후의 데이터
    alpha: 정규화 구간 1
    beta: 정규화 구간 2, 구간 정규화가 아닌 경우 사용 안 함
    type_flag: 정규화 알고리즘 선택 플래그 상수
'''

def draw_hist(hist, shape = (200, 256)):

    hist_img = np.full(shape, 255, np.uint8) # 200 x 256의 255 color Background
    cv2.normalize(hist, hist, 0, shape[0], cv2.NORM_MINMAX) # 최소값 0 , 최대값이 영상의 크기인 shape[0]이 되도록 정규화
    gap = hist_img.shape[1]/hist.shape[0] # 한 계급 너비

    for i, h in enumerate(hist):
        x = int(round(i*gap)) # 막대 사각형 시작 x좌표
        w = int(round(gap))

        # h : histogram value
        cv2.rectangle(hist_img, (x, 0, w, int(h)), 0, cv2.FILLED)

    return cv2.flip(hist_img, 0) # x축 기준으로 영상 상하 뒤집기 후 반환

result_img = draw_hist(hist2)

cv2.imshow("image", image)
cv2.imshow("result", result_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
