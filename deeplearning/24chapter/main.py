import torch

def dm03():
    t1 = torch.randint(1,10,size=(2,3,4))
    print(f"t1:{t1} shape:{t1.shape}")
    print("-" * 30)


    t2 = t1.transpose(0,1)
    print(f"t2:{t2} shape:{t2.shape}")


if __name__ == '__main__':
    dm03()
    