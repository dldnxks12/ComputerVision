# 카메라 속성 Setting 
# cv2.VideoCapture.get() -> attribute get
# cv2.VideoCapture.set() -> attribute set


# 카메라 속성 중에서 Zoom 과 Focus를 조정해본다. 

import cv2
from CV_utils.utils import put_string


def zoom_bar(value): # zoom call back 함수
    global capture
    capture.set(cv2.CAP_PROP_ZOOM, value)

def focus_bar(value): # focus call back 함수
    global capture
    capture.set(cv2.CAP_PROP_FOCUS, value)

capture = cv2.VideoCapture(0)
if capture.isOpened() == False:
    raise Exception("error")

capture.set(cv2.CAP_PROP_FRAME_WIDTH, 400)
capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 300)
capture.set(cv2.CAP_PROP_AUTOFOCUS,0) # 자동 초점 중지
capture.set(cv2.CAP_PROP_BRIGHTNESS, 100)

title = "Change Camera Properties"
cv2.namedWindow(title)
cv2.createTrackbar('zoom', title, 0, 10, zoom_bar)
cv2.createTrackbar('focus', title, 0, 10, focus_bar)

while True:
    ret, frame = capture.read()
    if not ret:
        break
    if cv2.waitKey(30) >= 0:
        break

    zoom = int(capture.get(cv2.CAP_PROP_ZOOM))
    focus = int(capture.get(cv2.CAP_PROP_FOCUS))

    put_string(frame, 'zoom : ', (10,240), zoom)
    put_string(frame, 'focus : ', (10,270), focus)
    cv2.imshow(title, frame)

capture.release()