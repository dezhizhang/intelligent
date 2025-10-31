class Student:
    name = None
    age = None
    __score = None

    def __init__(self,name,age):
        self.name = name
        self.age = age

    def show_info(self):
        print(f"name={self.name} age={self.age} score={self.__score}")

class Pupil(Student):
    def testing(self):
        print(f"{self.name} 小学生正在考试")


class Graduate(Student):
    def testing(self):
        print(f"{self.name} 大学生正在考试")

pu = Pupil("tom",22)
pu.testing()

gr = Graduate("jack",32)
gr.testing()
