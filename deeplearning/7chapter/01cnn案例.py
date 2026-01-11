import torch
import torch.nn as nn
from torchvision.datasets import CIFAR10
from torchvision.transforms import ToTensor
import torch.optim as optim
from torch.utils.data import DataLoader
import time
import matplotlib.pyplot as plt
from torchsummary import summary

BATCH_SIZE = 8


#1. 准备数据集
def create_dataset():
    # 获取训练集
    train_dataset = CIFAR10(root='./data', train=True, transform=ToTensor())
    # 获取测试集
    test_dataset = CIFAR10(root='./data', train=False, transform=ToTensor())
    # 返回数据集
    return train_dataset, test_dataset

class ImageModel(nn.Module):
    def __init__(self):
        super().__init__()

        # 第一个卷积层
        self.conv1 = nn.Conv2d(3,6,3,1,0)
        # 第一个池化层
        self.pool1 = nn.MaxPool2d(2,0)
        # 第一个隐藏层
        self.linear1 = nn.Linear(576,120)
        # 第二个隐藏层
        self.linear2 = nn.Linear(120,84)
        # 隐藏层3
        self.output = nn.Linear(84,10)

    # 定义反向传播
    def forward(self, x):

        # 分解版
        x = self.pool1(torch.relu(self.conv1(x)))
        # 第二层+池化层
        x = self.pool2(torch.relu(self.conv2(x)))
        # 表示自动计算
        x = x.reshape(x.size(0),-1)

        # 第三层，全连接层(加权求和) + 激层
        x = torch.relu(self.linear1(x))

        # 第四层 全连接层
        x = torch.relu(self.linear2(x))

        return self.output(x)


if __name__ == '__main__':
    train_dataset, test_dataset = create_dataset()







