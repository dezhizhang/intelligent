import pandas as pd

s = pd.Series({"a":1,"b":2,"c":3})
s.name = "test"

print(s.index)
print(s.values)
print(s.shape)
print(s.ndim)
print(s.size)
print(s.dtype)
print(s.name)
print(s.loc['a'])






