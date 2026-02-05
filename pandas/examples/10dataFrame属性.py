import pandas as pd

s1 = pd.Series([1,2,3,4,5])
s2 = pd.Series([6,7,8,9,10])

df = pd.DataFrame({"第一列":s1,"第二列":s2})

print(df.head())
print(df.tail())


