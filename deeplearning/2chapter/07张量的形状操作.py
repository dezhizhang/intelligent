import torch



def dm01():
    t1 = torch.randint(1,10,size=(2,3))

    print(f"t1:{t1} shape:{t1.shape}")

    # 在0维上添加维度
    t2 = t1.unsqueeze(0)
    print(f"t2:{t2} shape:{t2.shape}")

    # 在1维上添加维度
    t3 = t1.unsqueeze(1)
    print(f"t3:{t3} shape:{t3.shape}")


if __name__ == '__main__':
    dm01()
