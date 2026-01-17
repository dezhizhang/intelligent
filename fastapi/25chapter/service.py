

from model import Student

async def create_student(name:str,age:int = None,email:str = None) -> Student:
    try:
        student = await Student(name=name, age=age, email=email)
        return student
    except Exception as e:
        print(e)


