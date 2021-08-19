#### OpenCV에서 제공하는 통계 관련 함수

- page 190

---

1. 배열의 각 Channel 별로 원소들을 합해서 return 

        cv2.sumElems(src) -> retval
    
2. 배열 원소들의 Mean , Std return     
  
        cv2.meanStdDev() -> mean , stddev
    
3. 행렬의 각 행 or 각 열로 정렬

        cv2.sort() -> retval

4. 행렬을 열방향 / 행방향으로 옵션 상수에 따라 축소

        cv2.reduce() -> retval
...
