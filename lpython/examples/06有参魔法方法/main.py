

class Car:
    def __init__(self,color:str,number:int):
        self.color = color
        self.number = number


    def show(self):
        print(f"颜色：{self.color} 颜色:{self.number}")




c = Car("red",1)
c.show()

