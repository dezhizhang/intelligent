# class A:
#     aa = 5
#     def __init__(self, x,y):
#         self.x =x
#         self.y = y
#
# a = A(2,3)
#
# print(a.x, a.y,a.aa)

class A:
    aa = 5
    def __init__(self, x,y):
        self.x = x
        self.y = y

a = A(1,2)
a.aa = 100
print(a.x, a.y,a.aa)





