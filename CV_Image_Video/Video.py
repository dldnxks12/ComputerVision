'''
Video는 코덱(Codec)에 의해 해당 포맷에 맞게 압축해서 저장되고, 재생될 때 다시 압축을 해제한다.

    코덱(Codec)

        Video 신호를 압축하는 Coder 와 Video 신호를 압축해제하는 Decoder 의 합성어 


즉, Video file에서 영상 frame을 받아 영상처리를 하기 위해서는 Decoding 과정이 필요 (파일 포맷에 따른 코덱을 통해서 압축 해제해야함)


    OpenCV에서는 입력되는 영상을 쉽게 처리할 수 있도록 API 지원

    cv2.VideoCapture 클래스로 카메라나 동영상에서 frame을 읽어올 수 있다.
    cv2.VideoWriter  클래스로 행렬로 된 영상들을 동영상 파일로 만들 수 있다.
'''

# 카메라에서 frame 읽기

import cv2

def put_string(frame, text, pt, value, color =(120, 200, 90) ): # 문자열 출력 함수 
    text += str(value)
    shade = (pt[0]+2, pt[1]+2)
    font = cv2.FONT_HERSHEY_SIMPLEX
    cv2.putText(frame, text, shade, font, 0,7, (0,0,0), 2) # 그림자 효과
    cv2.putText(frame, text, pt, font, 0.7, color, 2) # 글자 적기 


capture = cv2.VideoCapture(0) # 0 번 카메라 연결

if capture.isOpened() == False:
    raise Exception("Error")

print("Width : %d" % cv2.VideoCapture.get(cv2.CAP_PROP_FRAME_WIDTH))
print("Height : %d" % cv2.VideoCapture.get(cv2.CAP_PROP_FRAME_HEIGHT))
print("노출 : %d" % cv2.VideoCapture.get(cv2.CAP_PROP_EXPOSURE))
print("밝기 : %d" % cv2.VideoCapture.get(cv2.CAP_PROP_BRIGHTNESS))

while True:
    ret ,frame = capture.read() # 카메라 영상 받기 , ret ? True or False 

    if not ret:
        break

    if cv2.waitKey(30) >= 0: # Space Bar 누르면 종료
        break

    exposure = capture.get(cv2.CAP_PROP_EXPOSURE) # 노출 값 get
    put_string(frame, 'EXPOSURE', (10,40), exposure)

    title = "View Frame From Camera"
    cv2.imshow(title, frame)

capture.release() # Camera  자원 return 