import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split  # 训练集和测试集分
from sklearn.linear_model import LogisticRegression   # 逻辑回归
from sklearn.metrics import accuracy_score  # 模型评估

def dm01_data_preprocess():
    # 1. 读取csv文件，获取到df对像
    churn_df = pd.read_csv('../assets/churn.csv')

    # 2. 因为churn和gender列是字符串，需要进行one-hot编码
    churn_df = pd.get_dummies(churn_df, columns=['Churn', 'gender'])

    # 3. 删除one-hot处理后的冗余列
    churn_df.drop(['Churn_No', 'gender_Male'], axis=1, inplace=True)
    # churn_df.info()
    # print(churn_df.head(5))

    # 4. 修改列表将Churn_Yes-> Flag 充当标签列
    churn_df.rename(columns={"Churn_Yes": "flag"}, inplace=True)

    # 5. 查看数据值分布
    print(churn_df.flag.value_counts())


def dm02_data_visualization():
    # 1. 读取csv文件获取df对像
    churn_df = pd.read_csv('../assets/churn.csv')
    # 2. 对object类型的列(数据)做one-hot编码处理
    churn_df = pd.get_dummies(churn_df, columns=['Churn', 'gender'])
    # 3. 删除one-hot处理后的冗余列
    churn_df.drop(['Churn_No', 'gender_Male'], axis=1, inplace=True)

    # 修改列表,将Churn_Yes-> flag 充当标签列
    churn_df.rename(columns={"Churn_Yes": "flag"}, inplace=True)

    # 4. 绘制图表
    sns.countplot(churn_df, x="Contract_Month", hue="flag")
    plt.show()


def dm03_logistic_regression():
    # 1. 加载数据集
    churn_df = pd.read_csv('../assets/churn.csv')
    # 2. 对object类型的列数据做one-hot编码
    churn_df = pd.get_dummies(churn_df, columns=['Churn', 'gender'])
    # 3. 删除one-hot处理后的冗余的列
    churn_df.drop(['Churn_No', 'gender_Male'], axis=1, inplace=True)
    # 4. 修改列名将Churn_Yes -> flag 充当标签列
    churn_df.rename(columns={"Churn_Yes": "flag"}, inplace=True)
    # 5. 特征提取
    x = churn_df[["Contract_Month","internet_other","PaymentElectronic"]]
    y = churn_df["flag"]

    # 6. 划分训练集与测试集
    x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.2,random_state=23)

    # 7. 模型训练
    estimator = LogisticRegression()
    estimator.fit(x_train,y_train)

    # 8. 模型预测
    y_pre = estimator.predict(x_test)

    # 9. 模型评估
    print(f"准确率:{estimator.score(x_test,y_test)}")
    print(f"准确率:{accuracy_score(y_test,y_pre)}")




if __name__ == '__main__':
    dm03_logistic_regression()
