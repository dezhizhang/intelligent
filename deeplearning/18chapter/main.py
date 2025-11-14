# import torch
#
# t1 = torch.tensor([
#     [1,2,3],
#     [4,5,6]
# ])
#
# print(f"t1:{t1.sum(0)}")
# print(f"t1:{t1.sum(1)}")
# print(f"t1:{t1.sum()}")
import torch


def dm01():
    t1 = torch.tensor([
        [1,2,3],
        [4,5,6]
    ])

    print(f"t1:{t1.sum(0)}")
    print(f"t1:{t1.sum(1)}")
    print(f"t1:{t1.sum()}")

def dm02():
    t1 = torch.tensor([
        [1,2,3],
        [4,5,6]
    ])

    print(f"t1:{t1.max(dim=0)}")
    print(f"t1:{t1.max(dim=1)}")
    print(f"t1:{t1.max()}")

def dm03():
    t1 = torch.tensor([
        [1,2,3],
        [4,5,6]
    ])

    print(f"t1:{t1.pow(2)}")
    print(f"t1:{t1.pow(3)}")
    print(f"t1:{t1.pow(1)}")


if __name__ == "__main__":
    dm03()
