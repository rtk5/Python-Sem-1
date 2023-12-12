#composition
class Salary:
    def __init__(self,pay):
        self.pay=pay
    def get_total(self):
        return(self.pay*12)
class Employee:
    def __init__(self,pay,bonus):
        self.pay=pay
        self.bonus=bonus
        self.obj_salary=Salary(self.pay)
    def annual_sal(self):
        return "Annual salary is"+str(self.obj_salary.get_total())
print(Employee(365.7,100).annual_sal())


        
