'''

Mouse Event는 사용자가 지정한 Callback 함수로 제어할 수 있다.

1. callback 함수정의
2. setMouseCallback() 함수를 통해 시스템에 등록
3. Mouse event 발생시키면 시스템이 callback 함수를 호출한다.

def setMouseCallback(windowname, onMouseEventFunction, param=None), return None

    onMouseEventFunction : 마우스 이벤트에 대한 처리와 제어를 구현하는 CallBack 함수 -> 우리가 정의
'''

import numpy as np
import cv2

def onMouse(event, x, y, flags, param): # event가 발생하는 마우스 커서 위치 (x,y)
    if event == cv2.EVENT_LBUTTONDOWN:
        print("마우스 왼쪽 버튼 누르기")
    elif event == cv2.EVENT_RBUTTONDOWN:
        print("마우스 오른쪽 버튼 누르기")
    elif event == cv2.EVENT_LBUTTONUP:
        print("마우스 오른쪽 버튼 떼기")
    elif event == cv2.EVENT_RBUTTONUP:
        print("마우스 오른쪽 버튼 떼기")

image = np.zeros((200,300),np.uint8)
image[:] = 255

title1, title2 = "Event1", "Event2"
cv2.imshow(title1, image) # 해당하는 window 창 안에서 마우스를 클릭해야 event가 발생한다. 
cv2.imshow(title2, image)

cv2.setMouseCallback(title1, onMouse)
cv2.waitKey(0)
cv2.destroyAllWindows()




