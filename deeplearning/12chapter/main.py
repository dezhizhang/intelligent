
import torch
import numpy as np


def dm01():
    t1 = torch.tensor([1,2,3,4,5])

    # 张量转numpy
    n1 = t1.numpy().copy()

    n1[0] = 100
    print(f"t1:{t1} type:{type(t1)}")
    print(f"n1:{n1} type:{type(n1)}")


# def dm02():
#     n1 = np.array([11,22,33])
#     print(f"n1:{n1} type:{type(n1)}")
#
#     # 把numpy转换成张量
#     t1 = torch.from_numpy(n1)
#     print(f"t1:{t1} type:{type(t1)}")

def dm02():
    n1 = np.array([11,22,33])
    print(f"n1:{n1} type:{type(n1)}")

    # 把numpy转换成张量
    t1 = torch.from_numpy(n1)
    print(f"t1:{t1} type:{type(t1)}")





if __name__ == '__main__':
    dm02()