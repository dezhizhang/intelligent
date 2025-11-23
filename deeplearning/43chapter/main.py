# 参数初始化
import torch.nn as nn

# def dm01():
#     # 创建线性层
#     linear = nn.Linear(5,3)
#     # 对权重进行实始化
#     nn.init.uniform_(linear.weight)
#
#     # 打印生成结果
#     # print(linear.weight)
#     print(linear.weight.data)
#     print(linear.bias.data)
#

def dm01():
    linear = nn.Linear(5,3)
    # 对权重进行初始化
    nn.init.uniform_(linear.weight)

    # 打印生成结果
    print(linear.weight.data)
    print(linear.bias.data)


# 固定初始化
# def dm02():
#     linear = nn.Linear(5,3)
#     nn.init.constant_(linear.weight,3)
#     nn.init.constant_(linear.bias,3)
#
#     print(linear.weight.data)
#     print(linear.bias.data)


# def dm02():
#     linear = nn.Linear(5,3)
#     nn.init.constant_(linear.weight,3)
#     nn.init.constant_(linear.bias,3)
#
#     print(linear.weight.data)
#     print(linear.bias.data)

# def dm03():
#     linear = nn.Linear(5,3)
#     nn.init.zeros_(linear.bias)
#     nn.init.zeros_(linear.weight)
#
#     print(linear.weight.data)
#     print(linear.bias.data)

def dm03():
    linear = nn.Linear(5,3)
    nn.init.zeros_(linear.bias)
    nn.init.zeros_(linear.weight)

    print(linear.weight.data)
    print(linear.bias.data)


# def dm04():
#     linear = nn.Linear(5,3)
#     nn.init.ones_(linear.weight)
#     print(linear.weight.data)

def dm04():
    linear = nn.Linear(5,3)
    nn.init.ones_(linear.weight)
    print(linear.weight.data)

# def dm05():
#     linear = nn.Linear(5,3)
#     nn.init.normal_(linear.weight)
#     print(linear.weight.data)

# def dm05():
#     linear = nn.Linear(5,3)
#     nn.init.normal_(linear.weight)
#     print(linear.weight.data)

def dm05():
    linear = nn.Linear(5,3)
    nn.init.normal_(linear.weight)
    print(linear.weight.data)

def dm06():
    linear = nn.Linear(5,3)

    nn.init.kaiming_uniform_(linear.weight)
    print(linear.weight.data)

# def dm07():
#     linear = nn.Linear(5,3)
#     nn.init.xavier_normal_(linear.weight)
#     print(linear.weight.data)
#
# def dm07():
#     linear = nn.Linear(5,3)
#     nn.init.xavier_normal(linear.weight)
#     print(linear.weight.data)
def dm07():
    linear = nn.Linear(5,3)
    nn.init.xavier_normal_(linear.weight)
    print(linear.weight.data)




if __name__ == '__main__':
    dm07()

