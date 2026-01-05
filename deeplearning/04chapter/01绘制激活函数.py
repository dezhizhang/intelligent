import torch.nn as nn


# 1. 均匀分布随机产生参数
def dm01():
    linear = nn.Linear(5,3)
    #  对权重进行初始化
    nn.init.uniform_(linear.weight)
    # 对偏置进行初始化
    nn.init.uniform_(linear.bias)

    print(linear.weight.data)
    print(linear.bias.data)

#2. 固定值初始化
def dm02():
    linear = nn.Linear(5,3)
    # 对权重进行随机初始化
    nn.init.constant_(linear.weight,3)
    # 对偏置进行随机初始化
    nn.init.constant_(linear.bias,3)
    print(linear.weight.data)
    print(linear.bias.data)


# 全0初始化
def dm03():
    linear = nn.Linear(5,3)
    # 对权重进行初始化全0初始化
    nn.init.zeros_(linear.weight)
    # 对偏置进行初始化全0初始化
    nn.init.zeros_(linear.bias)
    print(linear.weight.data)
    print(linear.bias.data)

# 全1进行初始化
def dm04():
    linear = nn.Linear(5,3)
    # 对权重进行初始化全0初始化
    nn.init.ones_(linear.weight)
    # 对偏置进行初始化全0初始化
    nn.init.ones_(linear.bias)
    print(linear.weight.data)
    print(linear.bias.data)

def dm06():
    linear = nn.Linear(5,3)
    nn.init.kaiming_normal(linear.weight)

    print(linear.weight.data)





if __name__ == '__main__':
    dm06()

