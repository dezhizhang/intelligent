class Student:
    name = None

    def say_hi(self):
        print(f"hello {self.name}")
    def say_hi2(self,msg):
        print(f"{self.name} {msg}")


stu = Student()
stu.name = "tom"

stu.say_hi()
stu.say_hi2("python")