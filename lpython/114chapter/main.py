class Student:
    name = None
    age = None
    tel = None
    def __init__(self,name,age,tel):
        self.name = name
        self.age = age
        self.tel = tel

stu = Student("张德志",32,"15992478448")
print(stu.name)

