# Jupyter or Corab에서는 OpenCV의 Imshow 보다 Matplotlib으로 이미지를 띄우는 것의 훨씬 편리하다.
# 간단하게 사용법을 익힌다. 

# axis , tight_layout, subplot .. 

import cv2
import matplotlib.pyplot as plt

image = cv2.imread("C:/Users/USER/Desktop/git/OpenCV/CV_Image_Video/1.jpg", cv2.IMREAD_COLOR)
if image is None:
    raise Exception("error")

rows, cols = image.shape[:2] # image.shape = (rows, cols, channels)

rgb_img = cv2.cvtColor(image, cv2.COLOR_BGR2RGB) # openCV는 imread시 RGB channel 순이 아니라 BGR channel 순으로 읽어들인다.
gray_img = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

flg = plt.figure(num = 1, figsize = (3,4)) # Size = 3 x 4
plt.imshow(image)
plt.title("fig1 - original bgr ")
plt.axis('off')
plt.tight_layout() # 축 없음, 여백 없음  #

flg = plt.figure(figsize=(6,4))
plt.suptitle('figure2 - pyplot image display')
plt.axis([0, cols, rows, 0 ]) # 축 범위 

plt.subplot(1,2,1)
plt.imshow(rgb_img)
plt.title('rgb color')

plt.subplot(1,2,2)
plt.imshow(gray_img, cmap = 'gray')
plt.title('gray_img2')

plt.show() # 그림 객체를 Window에 띄우기  -> Corab or Jupyter에서는 Cell Block에 띄워주기때문에 굳이 필요 x 




