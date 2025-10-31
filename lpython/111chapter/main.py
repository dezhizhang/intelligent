
def cal01():
    sum = 0
    for i in range(1,1001):
        sum += i
    print(sum)

def hi():
    print("hi python")

class Person:
    name = None
    age = None

    def ok(self):
        print("ok")


p = Person()
p.cal01 = cal01
p.hi = hi


p.hi()
p.cal01()

print(type(p.hi))
print(type(p.ok()))












