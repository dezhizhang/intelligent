from datetime import date


class User:
    def __init__(self, name, birthday):
        self.name = name
        self.birthday = birthday

    def __getattr__(self, name):

        return getattr(self.name,name)





if __name__ == '__main__':
    user = User('tom', date(year=2012, month=1, day=1))
    print(user.name)
    print(user.birthday)
    print(user.age)



