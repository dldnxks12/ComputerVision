# 하나의 그림에 여러 Subplot 나타내는 다른 방법
# 보간 이라는 것도 추가

import cv2
import matplotlib.pyplot as plt
import numpy as np

methods = ['none', 'nearest', 'bilinear', 'bicubic', 'spline16', 'spline36'] # Interpolation Methods

grid = np.random.rand(5,5)  # 5x5 2차원 Arr 생성

print(grid)
'''
[[0.2787404  0.7226907  0.24762855 0.21090613 0.33134379]
 [0.91449766 0.7517289  0.97902919 0.80434711 0.4798703 ]
 [0.55959675 0.46987741 0.68606962 0.5314458  0.72844866]
 [0.44193108 0.91695897 0.48590223 0.20743403 0.66763158]
 [0.19071168 0.27393143 0.6791189  0.88546878 0.73810201]]
'''

fig, axs = plt.subplots(nrows = 2, ncols = 3, figsize =(8,6)) # 가로 4개 세로 2개 이미지 넣을 것 

for ax, method in zip(axs.flat, methods):
    ax.imshow(grid, interpolation = method, cmap = 'gray')
    ax.axis('off')
    ax.set_title(method)

plt.tight_layout
plt.show()

