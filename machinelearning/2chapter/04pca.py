import numpy as np
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA


x = np.random.randn(1000,3)
print(x.shape)


# 使用pca进行
pca = PCA(n_components=2)
x_pca = pca.fit_transform(x)
print(x_pca.shape)


# 可视化
fig = plt.figure(figsize=(12,4))
ax1 = fig.add_subplot(121,projection='3d')
ax1.scatter(x[:,0],x[:,1],x[:,2],c="g")
ax1.set_title('Before PCA(3D)')
ax1.set_xlabel('PC1')
ax1.set_ylabel('PC2')
ax1.set_zlabel('PC3')

plt.show()


ax2 = fig.add_subplot(122)
ax2.scatter(x[:,0],x[:,1],c="g")

ax2.set_xlabel('PC1')
ax2.set_ylabel('PC2')
plt.show()





