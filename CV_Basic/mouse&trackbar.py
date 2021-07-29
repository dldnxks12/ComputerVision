'''

마우스 왼쪽 버튼을 클릭하면 영상의 밝기가 밝아지고, 오른쪽 버튼을 클릭하면 영상이 어두워지는 예제
trackbar의 위치도 같이 변화하도록 한다.

'''

import numpy as np
import cv2

def onChange(value):

    global image, title

    add_value = value - image[0][0]
    print("추가 화소값")
    image = image + add_value
    cv2.imshow(title, image)

def onMouse(event, x, y , flags, param):

    global title, image, name

    if event == cv2.EVENT_LBUTTONDOWN: # 왼쪽 버튼 -> trackbar 왼쪽으로
        if(image[0][0] < 246):
            image = image+10
            cv2.setTrackbarPos(title, name, image[0][0])
            cv2.imshow(title, image)
    elif event == cv2.EVENT_RBUTTONDOWN: # 오른쪽 버튼 -> trackbar 오른쪽으로
        if (image[0][0] > 10):
            image = image - 10
            cv2.setTrackbarPos(title, name, image[0][0])
            cv2.imshow(title, image)

image = np.zeros((200,500), np.uint8)

title = "trackbar Event"
name = "Mouse + Trackbar"
cv2.imshow(title, image)
cv2.setMouseCallback(title, onMouse)
cv2.createTrackbar(name, title, image[0][0], 255, onChange)

cv2.waitKey(0)
cv2.destroyAllWindows()
