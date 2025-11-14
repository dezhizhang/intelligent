import torch


# def dm01():
#     t1 = torch.tensor([[1,2,3],[4,5,6]])
#
#     t2 = torch.tensor([[1,2,3],[4,5,6]])
#
#     t3 = t1 * t2
#     print(f"t3:{t3} type:{type(t3)}")

def dm01():
    t1 = torch.tensor([[1,2,3],[4,5,6]])

    t2 = torch.tensor([[1,2,3],[4,5,6]])

    t3 = t1 * t2

    print(f"t3:{t3} type:{type(t3)}")

# def dm02():
#     t1 = torch.tensor([[1,2,3],[4,5,6]])
#
#     t2 = torch.tensor([[1,2],[3,4],[5,6]])
#
#     t3 = t1 @ t2
#     print(f"t3:{t3} type:{type(t3)}")

def dm02():
    t1 = torch.tensor([[1,2,3],[4,5,6]])

    t2 = torch.tensor([[1,2],[3,4],[5,6]])

    t3 = t1 @ t2
    print(f"t3:{t3} type:{type(t3)}")


if __name__ == "__main__":
    dm02()