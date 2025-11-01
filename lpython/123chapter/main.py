#
# class A:
#     n1 = 100
#
#     def run(self):
#         print("a run...")
#
# class B(A):
#     n1 = 200
#
#     def say(self):
#         print(f"父类的n1{A.n1} 本类的n1:{self.n1}")
#         A.run(self)
#
# b = B()
# b.say()
#


class A:
    n1 = 100
    __n2 = 600

    def run(self):
        print("a-run()...")

    def __jump(self):
        print("a-jump()...")

class B(A):
    def say(self):
        print(A.__n2)
        print(super().__n2)


b = B()
b.say()




