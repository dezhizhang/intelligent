class Company(object):
    def __init__(self, employee_list):
        self.employee_list = employee_list

    def __getitem__(self,item):
        return self.employee_list[item]

if __name__ == '__main__':

    company = Company([1,2,3])

    for item in company:
        print(item)

