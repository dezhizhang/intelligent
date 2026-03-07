

import numbers

class IntField:
    def __get__(self, instance, owner):
        return self.value
    def __set__(self, instance, value):
        if not isinstance(value,numbers.Integral):
            raise ValueError("int value need")

        self.value = value


    def __delete__(self, instance):
        pass


class User:
    age = IntField()


if __name__ == '__main__':
   user = User()
   user.age = "abc"
   print(user.age)








