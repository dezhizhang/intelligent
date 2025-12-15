import torch
import numpy as np

def dm01():
    t1 = torch.tensor(10)
    print(f"t1:{t1} type:{type(t1)}")
    print("*" * 30)

    data = [[1,2,3],[4,5,6]]
    t2 = torch.tensor(data)

    print(f"t2:{t2} type:{type(t2)}")
    print("*" * 30)

    data = np.random.randint(0,10,size=(2,3))
    t3 = torch.tensor(data)
    print(f"t3:{t3} type:{type(t3)}")


def dm02():
    t1 = torch.Tensor(10)
    print(f"t1:{t1} type:{type(t1)}")
    print("*" * 30)

    data = np.random.randint(0,10,size=(2,3))
    t2 = torch.Tensor(data)
    print(f"t2:{t2} type:{type(t2)}")

    print("*" * 30)

    t3 = torch.Tensor(2,3)
    print(f"t3:{t3} type:{type(t3)}")


if __name__ == '__main__':
    dm01()
