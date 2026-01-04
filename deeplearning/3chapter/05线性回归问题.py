import torch
from torch.utils.data import TensorDataset
from torch.utils.data import DataLoader
from torch import nn
from torch import optim
from sklearn.datasets import make_regression
import matplotlib.pyplot as plt


# plt.rcParams['font.sans-serif'] = ['SimHei']
# plt.rcParams['axes.unicode_mins'] = False


#1. 定义函数创建线性回归样本数据
def create_dataset():
    x,y,coef = make_regression(
        n_samples=100,
        n_features=1,
        noise=10,
        coef=True,
        random_state=3
    )

    x1 = torch.tensor(x,dtype=torch.float32)
    y1 = torch.tensor(y,dtype=torch.float32)
    return x1,y1,coef


if __name__ == '__main__':
    x,y,coef = create_dataset()
    print(f"x:{x},y:{y},coef:{coef}")
