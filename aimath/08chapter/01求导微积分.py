import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return x ** 2

x = np.linspace(0,3,100)
y = f(x)

x1 = 1
x2 = 1.1


y1 = f(x1)
y2 = f(x2)

plt.figure()
plt.plot(x,y)
plt.plot([x1,x2],[y1,y2])
plt.show()







