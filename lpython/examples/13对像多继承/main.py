class Master:
    def __int__(self):
        self.kongfu = '[古法煎饼果子配方]'

    def make_cake(self):
        print(f"运用:{self.kongfu}制作煎饼果子")


class School:
    def __int__(self):
        self.kongfu = '[数擎AI煎饼果子配方]'

    def make_cake(self):
        print(f"运用:{self.kongfu}制作煎饼果子")



class Student(Master, School):
    pass



s = Student()
s.make_cake()

