


class A(object):
    def __int__(self):
        print("A")


class B(A):
    def __int__(self):
        print("B")
        super().__init__()




if __name__ == '__main__':
    b = B()