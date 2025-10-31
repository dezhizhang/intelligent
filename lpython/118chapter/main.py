
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

    def getSlary(self):
        return self.__salary

clerk = Clerk("tom","前端开发",100)
print(clerk.getSlary())
print(clerk.getJob())


