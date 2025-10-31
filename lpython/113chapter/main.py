
class Person:
    name = None
    age = None

def f1(person):
    print(f"person的地址:{id(person)}")
    person.name = "jack"
    person.age += 1

p1 = Person()
p1.name = "tom"
p1.age = 22

print(f"p1的地址:{id(p1)} p1.name={p1.name} p1.age={p1.age}")
f1(p1)
print(f"p1的地址：{id(p1)} p1.name={p1.name} p1.age={p1.age}")


