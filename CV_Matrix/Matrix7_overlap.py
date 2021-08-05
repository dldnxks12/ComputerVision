# 행렬의 비트 연산을 이용해서 Color 영상을 오버랩

import numpy as np
import cv2

Image = cv2.imread("OpenCV/CV_Matrix/2.jpg", cv2.IMREAD_COLOR)
Logo  = cv2.imread("OpenCV/CV_Matrix/rgb1.jpg", cv2.IMREAD_COLOR)

# 처리할 이미지 
#cv2.imshow("image", Image)
#cv2.imshow("Logo", Logo)

if Image is None or Logo is None:
    raise Exception("error")

# Logo 이미지 이진화 --- cv2.threshold 이용

# ret, out = cv2.threshold  --- ( 220, list ) , ret은 threshold에 사용한 문턱 값
masks = cv2.threshold(Logo, 220, 255, cv2.THRESH_BINARY)[1] # --- 2원소 tuple 로 return  

# masks = np.array(masks)
# print(np.shape(masks))  (595, 842, 3)

b,g,r = cv2.split(masks) # b, g, r 모두 numpy type

fg_pass_mask = cv2.bitwise_or(b,g) # blue와 green에 해당 하는 값만 255
fg_pass_mask2 = cv2.bitwise_or(r, fg_pass_mask)
bg_pass_mask = cv2.bitwise_not(fg_pass_mask2)

cv2.imshow("fg_pass_mask2", fg_pass_mask2)
cv2.imshow("bg_pass_mask", bg_pass_mask)
# 이미지에 넣을 좌표 setting

(H,W) , (h,w) = Image.shape[:2], Logo.shape[:2]
x,y = (W-w)//2 , (H-h)//2

roi = Image[y:y+h, x:x+w]

foreground = cv2.bitwise_and(Logo, Logo, mask = fg_pass_mask2)
background = cv2.bitwise_and(roi,roi, mask = bg_pass_mask)
cv2.imshow("fg", foreground)
cv2.imshow("bg", background)

dst = cv2.add(foreground, background)

cv2.imshow("dst", dst)

Image[y:y+h, x:x+w] = dst # 처리한 부분 다시 이미지로 

cv2.imshow("Image", Image)

cv2.waitKey(0)
cv2.destroyAllWindows()