import numpy as np
import matplotlib.pyplot as plt

data = np.random.normal(loc=0.5,scale=0.5,size=10000)
mean = np.mean(data)
std = np.std(data)

print(f"均值u：{mean:4f} 标准差a:{std:4f} 方差a^2:{std*std:4f}")

plt.figure(figsize=(10,5))
plt.hist(data,bins=300,density=True)
plt.show()


