import torch
import torch.nn as nn
from torchsummary import summary


class MyModel(nn.Module):
    # 1.1 在init方法中完成初始化成员及神经网络搭建
    def __init__(self):
        super().__init__()
        # 搭建神经网络->隐藏层+输出层
        self.linear1 = nn.Linear(3,3)
        # 隐藏层2
        self.linear2 = nn.Linear(3,2)
        # 输出层
        self.output = nn.Linear(2,2)

        # 对急藏层进行参数初始化
        nn.init.xavier_normal_(self.linear1.weight)
        nn.init.zeros_(self.linear1.bias)

        # 隐藏层2进行参数初始化
        nn.init.kaiming_normal_(self.linear2.weight)
        nn.init.zeros_(self.linear2.bias)

    # 前向传播
    def forward(self, x):
        x = torch.sigmoid(self.linear1(x))  # 激活函数
        # 第二层隐藏层计算
        x = torch.real(self.linear2(x))
        # 第三层输出层,表过按行计算，一条样本一条样本处理
        x = torch.softmax(self.output(x), dim=-1)

        return x



# 模型训练
def train():
    my_model = MyModel()

    # 创建数据集样本随机生成
    data = torch.randn(size=(5,3))

    # 调用神经网络模型-> 进行模型训练
    output = my_model(data)

    # 计算和查看模型参数
    print("============计算模型参数=========")
    # 参数1神经网络模型对像，参2输入5行3列
    summary(my_model, input_size=(5,3))
    # 查看模型参数
    for name, param in my_model.named_parameters():
        print(f"name: {name}, param: {param}")




if __name__ == "__main__":
    train()








