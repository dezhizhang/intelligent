

class Company(object):
    def __init__(self, employee_list):
        self.employee_list = employee_list

    def __len__(self):
        return len(self.employee_list)


company = Company(['tom','jack','bob'])
print(len(company))