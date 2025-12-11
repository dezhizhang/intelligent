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


# 把 Sales 加回去，构成完整数据集
full_data = advertising.copy()  # 此时已去掉第一列和空值

# 计算整个 DataFrame 的相关系数矩阵（4×4）
corr_matrix = full_data.corr(method='pearson')

# 画热力图
plt.figure(figsize=(8, 6))
sns.heatmap(corr_matrix, annot=True, cmap="coolwarm", fmt=".2f", square=True)
plt.title("Correlation Matrix of All Variables")
plt.show()






