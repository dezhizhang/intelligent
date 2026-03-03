def ask(name="boby"):
    print(name)

# my_class = ask
# my_class("jack")


# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def speak(self):
#         print("%s is %d years old" % (self.name, self.age))
#
#
#
#
# my_class = Person("John", 36)
# my_class.speak()
#

def decorator_func():
    print("dec start")
    return ask

my_ask = decorator_func()
my_ask("tom")






