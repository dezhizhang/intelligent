# class Base:
#     n1 = 100
#     __n2 = 200
#
#     def __init__(self):
#         print("base 构造方法...")
#
#     def hi(self):
#         print("hi() 公共方法")
#
#     def __hello(self):
#         print("__hello() 私有方法")
#
# class Sub(Base):
#
#     def __init__(self):
#         print("sub构造方法")
#
#     def say_ok(self):
#         print("say_ok")
#         self.hi()
#
# sub = Sub()
# sub.say_ok()

class Base:
    n1 = 100
    __n2 = 200

    def __init__(self):
        print("base 构造方法...")

    def hi(self):
        print("hi() 公共方法")

    def __hello(self):
        print("__hello() 私有方法")

class Sub(Base):
    def __init__(self):
        print("sub构造方法")

    def say_ok(self):
        print("say_ok")
        self.hi()

sub = Sub()
sub.say_ok()





