import torch

def dm04():
    t1 = torch.randint(1,10,size=(2,3))
    # 判断张量是否连续
    print(t1.is_contiguous())

    # 通过view修改张量
    t2 = t1.view(3,2)
    print(f"t2:{t2} shape:{t2.shape}")
    print(t2.is_contiguous())

    # 通过transpose交换维度
    t3 = t1.transpose(0,1)
    print(f"t3:{t3} shape:{t3.shape}")
    print(t3.is_contiguous())

    t4 = t3.contiguous().view(2,3)
    print(f"t:{t4} shape:{t4.shape}")
    print(t4.is_contiguous())



if __name__ == "__main__":
    dm04()