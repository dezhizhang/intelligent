import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
advertising = pd.read_csv('advertising.csv')

# print(advertising.head())
# print(advertising.describe())
# print(advertising.shape)

# 数据预处理
advertising.drop(advertising.columns[0],axis=1,inplace=True)
# 去掉空值
advertising.dropna(inplace=True)

# 提取特征和标签
x = advertising.drop("Sales",axis=1)
y = advertising['Sales']

corr_matrix = x.corrwith(y,method='pearson')

sns.heatmap(corr_matrix,annot=True,cmap="coolwarm",fmt=".2f")
plt.title("Correlation Matrix")
plt.show()







