import torch


def dm01():
    t1 = torch.randint(1,10,size=(2,3))
    print(f"t1:{t1} shape:{t1.shape}")

    t2 = t1.reshape(3,2)
    print(f"t1:{t2.shape}")


if __name__ == '__main__':
    dm01()