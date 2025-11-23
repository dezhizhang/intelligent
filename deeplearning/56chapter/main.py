import torch
import matplotlib.pyplot as plt

ELEMENT_NUMBER = 30

def dm01():
    torch.manual_seed(0)
    temperature = torch.rand(size=[ELEMENT_NUMBER,])
    print(f"{temperature}")

    days = torch.arange(1,ELEMENT_NUMBER + 1,1)
    plt.plot(days, temperature,color="r")
    plt.scatter(days,temperature)
    plt.show()




if __name__ == '__main__':
    dm01()
