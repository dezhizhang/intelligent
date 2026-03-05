class User:
    def __init__(self, birthday):
        self.__birthday = birthday

    def get_birthday(self):
        return self.__birthday


if __name__ == "__main__":
    user = User(1993)
    print(user.get_birthday())

