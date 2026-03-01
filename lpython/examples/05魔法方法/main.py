
class Car:
    def __init__(self):

        self.color = "red"
        self.number = 3


    def show(self):
        print(f"颜色:{self.color}  轮胎数:{self.number}")



car = Car()
car.show()
