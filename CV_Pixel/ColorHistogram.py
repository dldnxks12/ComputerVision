# Color 영상의 색상 성분에 대한 히스토그램을 구해서 그래프로 그려보자
# 색상을 나타내기 위해 make_palette() 함수를 구현

import numpy as np
import cv2

def make_palette(rows): # hue channel 팔레드 행렬 생성 함수 , rows : 계급 수 (구간 수)
    hsv = np.full((rows,1,3), (255,255,255), np.uint8)  # rows x 1 x 3 channel 255 값으로된 행렬

    for i in range(0, rows): # 행 수 만큼 반복
        hue = round(i / rows*180) # 색상 계산
        hsv[i] = (hue, 255, 255) # HSV Color 지정 (hsv color, 채도, 휘도)

    return cv2.cvtColor(hsv, cv2.COLOR_HSV2BGR) # HSV color -> BGR color --- 모니터에 색상을 표시하기 위해 RGB로 변환 !

def draw_hue_hist(hist, shape = (200, 256, 3)): # Color Histogram 그리기 함수
    hsv_palette = make_palette(hist.shape[0]) # hist의 계급 수를 인자로 줌 --- 각 계급에 대한 색상을 반환받음
    hist_img = np.full(shape, 255 ,np.uint8) # shape 크기의 흰 배경 영상 --- histogram 그림 도화지
    cv2.normalize(hist, hist, 0, shape[0], cv2.NORM_MINMAX) # 정규화

    gap = hist_img.shape[1] / hist.shape[0] # 한 계급 크기 256 / 계급 수  == 계급 간 너비
    for i, h in enumerate(hist):
        x, w = int(round(i*gap)), int(round(gap)) # 계급 시작 x 좌표, w : 넓이
        # color : 팔레트의 한 원소 (색)
        color = tuple(map(int, hsv_palette[i][0])) # 사용하려면 정수형 튜플 type으로 바꿔야 함  -- hue 값 사용
        cv2.rectangle(hist_img, (x,0, w, int(h)), color, cv2.FILLED)

    return cv2.flip(hist_img, 0)


image = cv2.imread("./gy.jpg", cv2.IMREAD_COLOR)
if image is None:
    raise Exception("Error")

hsv_img = cv2.cvtColor(image, cv2.COLOR_BGR2HSV) # bgr -> hsv
hue_hist = cv2.calcHist([hsv_img], [0], None, [18], [0, 180]) # Hue 채널 Histogram 계산 0 channel = hue value

hue_hist_img = draw_hue_hist(hue_hist, (200, 360, 3))

cv2.imshow("image", image)
cv2.imshow("hue_img", hue_hist_img)
cv2.waitKey(0)
cv2.destroyAllWindows()




