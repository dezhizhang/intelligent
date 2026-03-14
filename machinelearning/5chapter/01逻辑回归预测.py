"""
案例:
    演示逻辑回归模型实现
原理:
    把线性回归处理的预测值->通过Sigmod激活函数 [0,1]

"""
import numpy as np
import pandas as pd
from sklearn.linear_model import LogisticRegression  # 逻辑回归
from sklearn.preprocessing import StandardScaler  # 模准化
from sklearn.model_selection import train_test_split  # 训练集和测试集分
from sklearn.metrics import accuracy_score  # 模型评估

# 1. 加载数据
data = pd.read_csv('../assets/breast-cancer-wisconsin.csv')

# 2. 数据处理
data.replace("?", np.nan, inplace=True)
# 缺失值处理-> 册除
data.dropna(axis=0, inplace=True)

# 3. 特征工程
x = data.iloc[:, :-1]
y = data.iloc[:, -1]
# 切割训练集和测试集
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=23)
transfer = StandardScaler()
x_train = transfer.fit_transform(x_train)
x_test = transfer.transform(x_test)

# 4. 模型训练
estimator = LogisticRegression()
estimator.fit(x_train, y_train)

# 5. 模型预测
y_pre = estimator.predict(x_test)

# 模型评估
print(f"预测前评估:{estimator.score(x_test, y_test)}")
print(f"预测后评估:{accuracy_score(y_test, y_pre)}")

