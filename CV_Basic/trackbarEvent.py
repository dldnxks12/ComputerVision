import numpy as np
import cv2

def onChange(value): # TrackBar Callback function
    global image, title

    add_value = value - image[0][0]
    print("추가 화소값 : ", value)
    image = image + add_value
    cv2.imshow(title, image) # trackbar Evnet가 발생할 때마다 window 창에 matrix 보여준다.

image = np.zeros((300,500), np.uint8)

title = 'Trackbar Event'
cv2.imshow(title, image)

cv2.createTrackbar('brightness', title, image[0][0], 255, onChange)
cv2.waitKey(0)
cv2.destroyAllWindows()
