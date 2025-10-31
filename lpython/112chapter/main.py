
class Person:
    name = None
    age = None

    def compare_to(self,other):
        return self.name == other.name and self.age == other.age


p = Person()
p.name = "tom"
p.age = 3

p2 = Person()
p2.name = "jack"
p2.age = 4

print(p.compare_to(p2))

