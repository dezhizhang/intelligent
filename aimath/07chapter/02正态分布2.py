import numpy as np
import matplotlib.pyplot as plt


def randCircle(center, radius, size=1000):
    points = np.random.rand(size * 5, 2) * 4 * radius - 2 * radius

    valid_points = []
    for point in points:
        if np.linalg.norm(point - center) <= radius:
            valid_points.append(point)

    valid_points = np.array(valid_points)
    return valid_points[:size]

data = []

for i in range(50):
    x = np.random.rand() * 10 - 5
    y = np.random.rand() * 10 - 5
    radius = 5 + np.random.rand() * 5

    t = randCircle((x, y), radius)
    data.append(t)

data0 = data[0]

data = np.concatenate(data, axis=0)
print(data.shape)

plt.figure(figsize=(15,15))


plt.subplot(2,2,1)
plt.scatter(data[:,0], data[:,1],s=1)

plt.show()



