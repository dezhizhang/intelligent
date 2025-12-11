import pandas as pd

x = [[5],[8],[10],[12],[15],[3],[7],[9],[14],[6]]
y = [55,65,70,75,80,50,60,72,80,58]

# 直接调用相关函数
x = pd.DataFrame(x)
y = pd.Series(y)

print(x.shape)
print(y.shape)

# 计算机关系数
print(x.corrwith(y,method='spearman'))

