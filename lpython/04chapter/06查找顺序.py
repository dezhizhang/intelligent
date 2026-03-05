class A(object):
    name = 'A'
    def __init__(self):
        self.name = "obj"

    def say(self):
        print(self.name)


a = A()
a.say()

print(a.name)
print(A.__mro__)
