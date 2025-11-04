import numpy as np
import matplotlib.pyplot as plt


x = np.arange(0,6,0.1)
y = np.sin(x)

# 定义导函数
y1 = np.cos(x)


plt.plot(x,y,label="sin(x)")
plt.plot(x,y1,label="cos(x)",linestyle="--")
plt.xlabel("x")
plt.ylabel("y")
plt.title("y=sin(x)")
plt.legend()
plt.show()




