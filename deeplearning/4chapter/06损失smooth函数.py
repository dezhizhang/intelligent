import torch
import matplotlib.pyplot as plt

ELEMENT_NUMBER = 30

def dm01():
    torch.manual_seed(0)
    # 生产30天的随机温度
    temperature = torch.randn(size=[ELEMENT_NUMBER,]) * 10

    # 绘制平均温度
    days = torch.arange(1,ELEMENT_NUMBER + 1,1)
    plt.plot(days, temperature,color='r')
    plt.scatter(days, temperature)
    plt.show()



if __name__ == '__main__':
    dm01()