import torch


def dm01():
    t1 = torch.arange(0,10,2)
    print(f"t1:{t1} type:{type(t1)}")
    print("*" * 30)

    t2 = torch.linspace(1,10,4)
    print(f"t2:{t2} type:{type(t2)}")


# def dm02():
#     torch.manual_seed(42)
#     t1 = torch.randn(size=(2,3))
#     print(f"t1:{t1} type:{type(t1)}")
#
#     # 创建整数随机张量
#     t2 = torch.randint(low=0,high=10,size=(2,5))
#     print(f"t2:{t2} type:{type(t2)}")

def dm02():
    torch.manual_seed(42)
    t1 = torch.randn(size=(2,3))

    # 创建整数随机张量
    t2 = torch.randint(low=0,high=10,size=(2,5))
    print(f"t1:{t2} type:{type(t2)}")





if __name__ == "__main__":
    dm02()

