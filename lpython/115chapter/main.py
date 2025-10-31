# class Cat:
#     name = None
#     age = None
#
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
#


class Person:
    def __init__(self,name,age):
        print(f"__init__执行了...{name}{age}")
        self.name = name
        self.age = age

p1 = Person("tom",22)

print(p1.name)
print(p1.age)




