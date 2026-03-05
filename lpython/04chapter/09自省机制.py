class Person:
    name = "user"

class Student(Person):
    def __init__(self, school_name):
        self.school_name = school_name


if __name__ == "__main__":
    user = Student("数擎")

    print(user.__dict__)
    print(user.name)
    print(dir(user))




