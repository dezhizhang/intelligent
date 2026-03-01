
class Car:

    def __init__(self,color,number):
        self.color = color
        self.number = number


    def __str__(self):
       return f"颜色{self.color},轮胎数:{self.number}"


car = Car("红色",4)
print(car)
