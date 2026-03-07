import matplotlib.animation
import matplotlib.pyplot as plt
import numpy as np

plt.rcParams['animation.html'] = "jshtml"
plt.ioff()

points = np.array([
    [0,0],
    [1,0],
    [1,1],
    [0,1],
    [0,0]
])

start = 1
end = 3
frames = 11
step = (end - start) / (frame - 1)

def animate(t):
    plt.cla()
    T = start + step * t

    transform_points = T * points
    plt.xlim(-0.1,5)
    plt.ylim(-0.1,5)
    plt.gca().set_aspect('equal', adjustable='box')
    plt.plot(transform_points[:, 0], transform_points[:, 1], 'ro-')

matplotlib.animation.FuncAnimation(fig,animate,frames=frames,interval=step)