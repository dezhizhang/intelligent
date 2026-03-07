def create_class(name):
    if name == "user":
        class User:
            def __init__(self, age):
                self.age = age


            def get_age(self):
                return self.age

        return User
    elif name == 'company':
        class Company:
            def __init__(self, age):
                self.age = age

        return Company


if __name__ == '__main__':
    my_class = create_class('user')
    my_class.age = 20

    my_class.get_age()



