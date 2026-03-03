class Company(object):
    def __init__(self, employee_list):
        self.employee_list = employee_list

    def __getitem__(self, item):
        return self.employee_list[item]


company = Company(['tom','jack','bob'])

for employee in company:
    print(employee)


