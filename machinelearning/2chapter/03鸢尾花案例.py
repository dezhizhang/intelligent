"""
案例:通过KNN算法实现鸢尾花的分类操作
回顾：机器学习项目研发流程
    1. 加载数据
    2. 数据预处理
    3. 特征工程
    4. 模型训练
    5. 模型预测
"""

from sklearn.datasets import load_iris
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import StandardScaler  # KNN算法 分类对像
from sklearn.metrics import accuracy_score  # 模型评估


def dm01_load_iris():
    # 1. 加载数据集
    iris_data = load_iris()
    # 2. 查看数据集
    # print(f"数据集:{iris_data}")
    # 3. 查看所有的键
    # print(f"数据集所有的键:{iris_data.keys()}")
    # print(f"特征对应的名称:{iris_data.feature_names}")
    # print(f"标签对应的名称:{iris_data.target_names}")
    # print(f"数据描述信息:{iris_data.DESCR}")
    # print(f"数据集的框架:{iris_data.frame}")
    # print(f"数据集的文件名:{iris_data.filename}")


# 2. 定义函数，绘制数据集的散点图
def dm02_load_iris():
    # 1. 加载数据集
    iris_data = load_iris()

    # 2. 转换成DataFrame对像
    iris_df = pd.DataFrame(iris_data.data, columns=iris_data.feature_names)
    print(iris_df)
    # 3. 给df对像新增1列-> 标签列
    iris_df['label'] = iris_data.target

    # 4. 绘制散点图
    sns.lmplot(data=iris_df, x='sepal length (cm)', y='sepal width (cm)', hue='label', fit_reg=False)

    plt.title("iris dataset")
    plt.tight_layout()
    plt.show()


# 3. 定义函数，切分训练集和测试集
def dm03_split_train_test():
    # 1. 加载数据集
    iris_data = load_iris()

    # 2. 数据预处理,从150个特征和标签中，按照8:2的比例，来切分
    x_train, x_test, y_train, y_test = train_test_split(
        iris_data.data,
        iris_data.target,
        test_size=0.2,
        random_state=23
    )

    # 3. 打印切割后的结果
    print(f"训练集的特征:{x_train} 个数:{len(x_train)}")
    print(f"训练集的标签:{x_test} 个数:{len(x_test)}")
    print(f"测试集的特征:{x_test} 个数:{len(x_test)}")
    print(f"测试集的标签:{y_test} <UNK>:{len(y_test)}")


# 定义函数，实现鸢尾花案例-> 加载数据、数据预处理、特征工程、模型训练、模型评估、模型预测
def dm04_iris_evaluate_test():
    # 1. 加载数据
    iris_data = load_iris()
    # 2. 数据预处理
    x_train, x_test, y_train, y_test = train_test_split(
        iris_data.data,
        iris_data.target,
        test_size=0.2,
        random_state=23
    )
    # 3. 特征工程,
    # 3.1 创建标准化对像
    transfer = StandardScaler()
    # 3.2 对特征列进行标准化
    x_train = transfer.fit_transform(x_train)
    # transform 只有转换，该函数适用于重复标准化动时
    x_test = transfer.transform(x_test)

    # 4. 模型训练
    # 4.1 创建模型对像
    estimator = KNeighborsClassifier(n_neighbors=3)
    # 4.2 具体的训练模型动作
    estimator.fit(x_train, y_train)

    # 5.模型预测
    y_pre = estimator.predict(x_test)
    print(f"预测结果为:{y_pre}")

    # 模型评估
    print(f"正确率:{estimator.score(x_test, y_test)}")



if __name__ == '__main__':
    # dm01_load_iris()
    # dm02_load_iris()
    dm04_iris_evaluate_test()
