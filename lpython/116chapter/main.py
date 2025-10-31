
class Clerk:
    name = None
    __job = None
    __salary = None

    def __init__(self,name,job,salary):
        self.name = name
        self.__job = job
        self.__salary = salary

    def getJob(self):
        return self.__job

    def getSalary(self):
        return self.__salary


clerk  = Clerk("tom","前端工程师",1000)
print(clerk.getJob())
print(clerk.getSalary())


