# python

## 类

### 简单类

```python
class Student:
    name = None
    gender = None
    age = None


stu = Student()
stu.name = "tom"
stu.age = 22
stu.gender = "男"

print(stu.name)
print(stu.gender)
print(stu.age)
```

### 类的成员

```python
class Student:
    name = None

    def say_hi(self, msg):
        print(f"{self.name} {msg}")


stu = Student()
stu.name = "tom"
stu.say_hi("hello")

```