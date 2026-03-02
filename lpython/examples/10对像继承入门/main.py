class Father:
    def __init__(self):
        self.gender = "男"

    def walk(self):
        print("饭后走一走")


class Son(Father):
    pass


s = Son()
print(s.gender)
s.walk()

