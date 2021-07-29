'''
event를 처리하기 위해 callback 함수를 사용한다. (키보드 이벤트, 마우스 이벤트, trackbar, ... )
    callback : 개발자가 직접 함수를 호출하는 것이 아니라, 어떤 이벤트가 발생하면 시스템이 개발자가 등록함 함수를 호출해주는 것

# OpenCV 에서의 event 처리

OpenCV에서는 callback함수 대신 waitKey() 또는 waitKeyEx() 함수를 통해 event를 처리한다.

1. waitKey() : delay(ms) 시간만큼 키 입력을 대기하고, 키 이벤트가 발생하면 해당 키 값을 반환
    delay <= 0 : 무한 대기
    delay > 0  : 지연 시간 안에 키 입력 없으면 -1 반환
2. waitkeyEx(): waitkey()와 동일하지만 return으로 전체 키 코드를 반환 (화살표 키 등을 입력받을 때 사용)

'''

# 1. Keyboard Event with waitkeyEx()
import numpy as np
import cv2

# ord() : 문자 to ASCII CODE
switch_case = {
    ord('a') : "a키 입력",
    ord('b') : "b키 입력",
    0x41 : "A키 입력",
    int("0x42",16) : "B키 입력",
    2424832 : "왼쪽",
    2490368 : "위쪽",
    2555904 : "오른쪽",
    2621440 : "아래쪽"
}

image = np.ones((200,300), np.float)
cv2.imshow("KeyboardEvent", image)

while True:
    key = cv2.waitKeyEx(100) # key event 발생 시 해당 키 값 return 
    if key == 27: # ESC Key
        break
    try:
        result = switch_case[key] # 해당 key에 대한 value return
        print(result)
    except KeyError:
        result = -1

cv2.destroyAllWindows()
