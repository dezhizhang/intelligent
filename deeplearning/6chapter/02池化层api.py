import torch
import torch.nn as nn


def dm01():
    inputs = torch.tensor([
        [
            [0,1,2],
            [3,4,5],
            [6,7,8]
        ]
    ])

    # 创建最大池化层
    pool1 = nn.MaxPool2d(2,1,0)
    outputs = pool1(inputs)

    print(f"outputs shape: {outputs}")





if __name__ == '__main__':
    dm01()