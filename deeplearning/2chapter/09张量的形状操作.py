import torch



def dm01():
    t1 = torch.randint(1,10,size=(2,3))

    t2 = t1.view(3,2)
    print(f"t2:{t1.shape} t2:{t1.shape}")



if __name__ == '__main__':
    dm01()