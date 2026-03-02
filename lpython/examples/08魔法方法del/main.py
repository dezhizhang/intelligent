class Car:
    def __init__(self,brand):
        self.brand = brand


    def __str__(self):
        return f"品牌:{self.brand}"

    def __del__(self):
        print(f"删除对像:{self.brand}")


car = Car("华为 ")

del car

