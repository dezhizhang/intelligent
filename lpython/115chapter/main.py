class Student:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"name={self.name},age={self.age}"

stu = Student("周杰伦",31)
print(stu.name)




