import pandas as pd

s = pd.Series([1,3,4,5],index=['a','b','c','d'],name='series')

print(s.index)
print(s.values)
print(s.shape)
print(s.ndim)
print(s.size)
print(s.dtype)
print(s.loc['a':'c'])
print(s.iloc[1])
print(s.at['a'])








