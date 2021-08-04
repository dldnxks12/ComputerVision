# 카메라 frame -> 동영상으로 저장

import cv2

capture = cv2.VideoCapture(0) # 0번 카메라 

if capture.isOpened() == False:
    raise Exception("error")  # c 에서는 perror로 바로 stderr로 보낸다

fps    = 29.97  # frame per second
delay  = round(1000/fps) # frame 간 delay
size   = (640,360)
fourcc = cv2.VideoWriter_fourcc(*'DX50') # 압축 Codec 설정 - Video를 만들어 내보내는 것이므로 Coder 과정 필요

capture.set(cv2.CAP_PROP_ZOOM, 1)
capture.set(cv2.CAP_PROP_FOCUS, 0)
capture.set(cv2.CAP_PROP_FRAME_WIDTH, size[0])
capture.set(cv2.CAP_PROP_FRAME_HEIGHT, size[1])

writer = cv2.VideoWriter("OpenCV/CV_Image_Video/test_video.avi", fourcc, fps, size)
if writer.isOpened() == False:
    raise Exception("error")

while True:
    ret, frame = capture.read()

    if not ret:
        break

    if cv2.waitKey(30) >= 0:
        break

    writer.write(frame) # Frame을 Video로 저장
    cv2.imshow("View Frame from Camera", frame)

capture.release()
writer.release()

