from sklearn.feature_selection import VarianceThreshold
import numpy as np

a = np.random.randn(100)
print(np.var(a))

# b = np.random.randn(100) * 0.1
b = np.random.normal(5,0.1,size=100)

print(np.var(b))


x = np.vstack((a,b)).T

print(x.shape)


vt = VarianceThreshold(0.01)
x_filtered = vt.fit_transform(x)
print(x_filtered.shape)
print(x_filtered)

