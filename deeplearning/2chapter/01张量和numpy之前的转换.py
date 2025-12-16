import torch
import numpy as np

def dm01():
    t1 = torch.tensor([1,2,3,4,5])
    print(f"t1:{t1} type:{type(t1)}")

    # 转成张量
    n1 = t1.numpy().copy()
    print(f"n1:{n1} type:{type(n1)}")



def dm02():
    n1 = np.array([11,22,33])
    print(f"n1:{n1} type:{type(n1)}")

    # 转换成tensor
    t1 = torch.from_numpy(n1)
    print(f"t1:{t1} type:{type(t1)}")

    t2 = torch.tensor(n1)
    print(f"t2:{t2} type:{type(t2)}")



if __name__ == "__main__":
    dm02()

