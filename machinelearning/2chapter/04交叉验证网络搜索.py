"""
案例：演示网格搜索和交叉验证
交叉验证解释：
    原理:
        把数据分成n份，例如分成4份
        第1次：把第1份数据作为验证集（测试集）其它作为训练集，训练模型，模型预测获取准确率

    目的:
        为了让模型的最终结果更准确
网格搜索
    目的/作用
        寻找最优超参数
    原理：
        接收超参可能出现的值，然后针对于超参的第个值进行交叉验证获取到最优的超参组合

    超参数:
        需要用户手录入的数据，不同的超参（组合）,可能会影响模型的最终评测结果

"""
from sklearn.datasets import load_iris
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import StandardScaler  # KNN算法 分类对像
from sklearn.metrics import accuracy_score  # 模型评估

# 1. 加载数据
iris_data = load_iris()

# 2. 数据预处理
x_train, x_test, y_train, y_test = train_test_split(
    iris_data.data,
    iris_data.target,
    test_size=0.2,
    random_state=22
)

# 3. 特征工程
transfer = StandardScaler()
x_train = transfer.fit_transform(x_train)
x_test = transfer.transform(x_test)

# 4. 模型训练
estimator = KNeighborsClassifier(n_neighbors=3)
# 定义字曲，记录超参可能出现的情况
param_dict = {'n_neighbors': [i for i in range(1, 11)]}
# 创建GridSearchCV -> 寻找最优超参，使用网格搜索+交叉验证方式
estimator = GridSearchCV(estimator, param_dict, cv=4)
# 模型训练
estimator.fit(x_train, y_train)

# print(f"最优评份:{estimator.best_score_}")
# print(f"最优超参组合:{estimator.best_params_}")
# print(f"最优的估计器对像:{estimator.best_estimator_}")
# print(f"具体的交叉验证结果:{estimator.cv_results_}")

# 5. 模型评估
estimator = KNeighborsClassifier(n_neighbors=5)
estimator.fit(x_train, y_train)

# 6. 模型预测
y_pre = estimator.predict(x_test)
print(f"准确率:{accuracy_score(y_test, y_pre)}")


