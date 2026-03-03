class Mater:
    def __int__(self):
        self.kongfu = ['古法']

    def make_cake(self):
        print(f"运用{self.kongfu}<UNK>")


class School(Mater):
    def __int__(self):
        pass
        self.kongfu = ['独创']
    def make_cake(self):
        Mater.make_cake(self)




if __name__ == '__main__':
    s = School()
    s.make_cake()


