import numpy as np
import matplotlib.pyplot as plt


def min_max_normalize(data):
    return (data - np.min(data)) / (np.max(data) - np.min(data))


x = np.linspace(-100,20,1000)
y = min_max_normalize(x)

plt.scatter(x, y, s=1)
plt.title('min max normalize')
plt.xlabel('x')
plt.ylabel('y')
plt.show()





