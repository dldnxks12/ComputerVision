# Drawing

import numpy as np
import cv2

blue, green, red = (255,0,0) , (0,255,0), (0,0,255)

image = np.zeros((400,600,3), np.uint8)  # 400x600x1이 아니라 400x600x3? -> 3개의 color channel을 의미
image[:] = (255,255,255)

pt1, pt2 = (50,50), (250,150)
pt3, pt4 = (400,150), (500,50)
roi = (50,200,200,100) # restrict of interest

# Line, Rectangle , 시작좌표 : 좌측 상단

cv2.line(image,pt1,pt2,red)
cv2.line(image,pt3,pt4,green,3, cv2.LINE_AA)

cv2.rectangle(image, pt1, pt2, blue, 3, cv2.LINE_4)
cv2.rectangle(image, roi, green, cv2.FILLED)

title1 = "line and recntangle"

# Circle
center = (150,150)
radius = 50
cv2.circle(image, center, radius, red)

# Ellipse
center = (200,200)
axes = (50,100)
angle = 0
startAngle = 0
endAngle = 180

cv2.ellipse(image, center, axes, angle, startAngle, endAngle, red)


# Text , 시작좌표 : 좌측 하단
cv2.putText(image, "hello", (100,100), cv2.FONT_HERSHEY_DUPLEX, 2, (100,100,100))


cv2.imshow(title1, image)
cv2.waitKey(0)
cv2.destroyAllWindows()

