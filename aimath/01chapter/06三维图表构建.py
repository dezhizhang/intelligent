import matplotlib.pyplot as plt
import numpy as np
import matplotlib

x = np.linspace(-2,2,50)
y = x.copy()

x,y = np.meshgrid(x,y)
z = np.exp(-(x ** 2 + y ** 2))

fig = plt.figure()
ax = fig.add_subplot(111,projection='3d')
ax.plot_surface(x,y,z,cmap=matplotlib.cm.hot)
plt.show()
