#### Computer Vision의 가장 기본이 되는 Pixel을 다루는 방법

---



- 행렬 가감법에서의 주의점 - OpenCV와 Numpy에서 0 ~ 255 사이의 Pixel 값 처리 방식의 차이점 

1. OpenCV의 Saturation 방식

        255 + 100 = 255 (Saturation)
        100 - 200 = 0 

2. Numpy의 Modulo 방식

        255 + 100 = (355%256) = 104 (modulo)
