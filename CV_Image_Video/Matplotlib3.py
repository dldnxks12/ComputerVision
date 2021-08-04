# Graph 그리기
# Figure 저장하기
# Figure Axis 범위 지정하기

import numpy as np
import matplotlib.pyplot as plt

x = np.arange(10)  # 1 ~ 10 
y = np.arange(10)
y2 = np.arange(10)**2
y3 = np.random.choice(50, size = 10)

plt.figure(figsize = (5,3))
plt.plot(x,y, 'b--' , linewidth = 2)
plt.plot(x,y2, 'go-' , linewidth = 3)
plt.plot(x,y3, 'c+-' , linewidth = 5)

plt.title("Line Examples")
plt.axis([0,10 , 0,80])
plt.tight_layout()
plt.savefig(fname = 'sample.png', dpi = 300)
plt.show()