class Cat:
    name = None
    age = None
    def hi(self):
        name = "皮皮"
        print(f"name={name}")
        print(f"name={self.name}")


cat = Cat()
cat.hi()
