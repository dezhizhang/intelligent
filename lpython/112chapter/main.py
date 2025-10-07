class Student:
    name = None
    def say_hi(self,msg):
        print(f"{self.name} {msg}")

stu = Student()
stu.name = "tom"
stu.say_hi("hello")


