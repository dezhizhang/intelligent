

import torch
import torch.nn as nn
from torchsummary import summary


'''
    1. 准备数据
    2. 搭建神经网络
    3. 模型训练
    4. 模型测试

'''

class ModelDemo(nn.Module):
    def __init__(self):
        super(ModelDemo, self).__init__()
        self.linear1 = nn.Linear(3,3)
        self.linear2 = nn.Linear(3,2)
        self.output = nn.Linear(2,2)

        # 初始化
        nn.init.xavier_normal_(self.linear1.weight)
        nn.init.zeros_(self.linear1.bias)

        nn.init.kaiming_uniform_(self.linear2.weight)
        nn.init.zeros_(self.linear2.bias)

    # 正确放到类内部
    def forward(self, x):
        x = torch.sigmoid(self.linear1(x))
        x = torch.relu(self.linear2(x))
        x = torch.softmax(self.output(x), dim=1)
        return x




# 模型训练
def train():
    # 创建模型对像
    model = ModelDemo()
    data = torch.randn(size=(5,3))

    # 调用神经网格模型-> 进行模型训练
    output = model(data)
    print(f"output:{output}")
    print(f"output.shape:{output.shape}")
    print(f"output.requires_grad:{output.requires_grad}")

    # 计算和查看模型参数
    print("=========================计算模型参数=========================")
    # 神经网络模型对像,输入数据的维度
    summary(model,input_size=(5,3))
    for name,param in model.named_parameters():
        print(f"name:{name} param:{param.shape}")




if __name__ == '__main__':
    train()



