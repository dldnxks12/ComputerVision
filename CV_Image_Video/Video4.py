'''
# Video에서 frame을 가져온 후 행렬에 저장해보자 
# frame을 행렬로 저장할 경우 손쉽게 이미지 처리를 수행할 수 있다. 

# frame 0 ~ 99 -> 처리 x
# frame 100 ~ 199 -> frame 별 화소의 파란색 성분에 100을 더해서 영상을 더 푸르게 만듦
# frame 200 ~ 299 -> frame 별 화소의 녹색 성분에 100을 더해서 영상을 더 녹색으로 만듦
# frame 300 ~ 399 -> frame 별 화소의 빨간색 성분에 100을 더해서 영상을 더 빨갛게 만듦

'''

#--- 사용 함수 ---#

# cv2.split()
# cv2.add()
# cv2.merge()


import cv2
from CV_utils.utils import put_string

capture = cv2.VideoCapture(0)
if capture.isOpened() == False:
    raise Exception("error")

frame_delay = capture.get(cv2.CAP_PROP_FPS)
delay = int(1000/frame_delay)
frame_cnt = 0

while True:

    ret, frame = capture.read()

    if not ret:
        break

    if cv2.waitKey(delay) >= 0: # 지정한 delay보다 frame이 들어오는 시간이 길다면? 
        break

    blue, green, red = cv2.split(frame) # 3 channel frame -> 1channel로 분리 color channel을 각 gray channel로 (blue, green red) 
    frame_cnt += 1

    if 100 <= frame and frame < 200:
        cv2.add(blue, 100, blue) # add(더할 이미지, 더하는 값, 출력 이미지)
    elif 200 <= frame and frame < 300:
        cv2.add(green, 100, green)
    elif 300 <= frame and frame < 400:
        cv2.add(red, 100, red)        

    frame = cv2.merge( [blue, green, red] )  # 3 channel로 나누었던 영상들 다시 Merge

    put_string(frame, 'frame_cnt: ', (20,30), frame_cnt)
    cv2.imshow("Read Video File",frame)

capture.release()