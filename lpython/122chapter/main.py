class A:
    n1 = 100
    def sing(self):
        print("a sing() ...",self.n1)

class B:
    n2 = 200
    def dance(self):
        print("b dance...",self.n2)

class C(A,B):
    pass

c = C()
c.dance()
c.sing()












