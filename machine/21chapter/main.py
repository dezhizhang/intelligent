from sklearn.datasets import load_iris
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split


# 定义函数
def dm01_load_iris():
    # 加载数据集
    iris_data = load_iris()
    # 查看数据集
    print(f'查看数据集的所有键:{iris_data.keys()}')
    # 查看数据集对应
    print(f'数据集的值:{iris_data.data}')
    print(f'集体的标签:{iris_data.target[:5]}')
    print(f'数据集的文件名:{iris_data.filename}')
    print(f'数据集的模型:{iris_data.data_module}')



def dm02_show_iris():
    # 加载数据
    iris_data = load_iris()
    # 把数据集转换成DataFrame
    iris_df = pd.DataFrame(iris_data.data,columns=iris_data.feature_names)
    # 给df 新增1列-标签列
    iris_df['label'] = iris_data.target

    # 绘制散点图
    sns.lmplot(data=iris_df,x = 'sepal length (cm)',y='sepal width (cm)',hue='label',fit_reg=True)
    plt.title('iris data')
    plt.show()


def dm03_show_iris():
    # 加载数据
    iris_data = load_iris()
    # 数据预处理
    x_train,x_test,y_train,y_test = train_test_split(iris_data.data,iris_data.target,test_size=0.2,random_state=23)
    print(f"训练集特征:{x_train} 个数{len(x_train)}")
    print(f"测试集特征:{x_test} 个数{len(x_test)}")



if __name__ == "__main__":
    dm03_show_iris()
