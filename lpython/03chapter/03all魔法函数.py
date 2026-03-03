class Company(object):
    def __init__(self, employee_list):
        self.employee_list = employee_list

    def __str__(self):
        return ",".join(self.employee_list)



company = Company(['tom','jack','bob'])
print(company)

