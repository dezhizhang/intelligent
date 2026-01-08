import torch
import torch.nn as nn
import matplotlib.pyplot as plt


def dm01():
    # 加载rgb真彩图
    img = plt.imread('./img.jpg')

    # 打印到的读取信息
    # print(f"img.shape: {img.shape}")

    # 把图像的形状从HWC->CHW
    img2 = torch.tensor(img,dtype=torch.float32)

    img2 = img2.permute(2,0,1)

    # 转换图形的通道
    img3 = img2.unsqueeze(0)

    # 创建卷积层对像，提取特征图
    conv = nn.Conv2d(3,4,3,2,0)

    # 具体的卷积计算
    conv_img = conv(img3)

    # 打印卷积后的结果
    print(f"conv_img shape: {conv_img.shape}")



if __name__ == '__main__':
    dm01()