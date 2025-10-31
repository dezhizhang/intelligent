class Clerk:
    name = None
    __job = None
    __salary = None

    def __init__(self,name,job,salary):
        self.name = name
        self.__job = job
        self.__salary = salary
    def get_job(self):
        return self.__job
clerk = Clerk("tom","前端开发",1000)
clerk.__job = "go 工程师"
print(f"job={clerk.__job}")
print(f"job={clerk.get_job()}")

