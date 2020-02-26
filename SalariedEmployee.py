#Import Employees class
from Employee import*
#Class is derived from Employee class
class SalariedEmployee(Employee):
    #Constructor that takes in id number, first and last name, months worked and monthly salary
    def __init__(self, id, fname, lname, monthsWorked, monthlySalary):
        Employee.__init__(self, id, fname, lname)
        self.salary = monthlySalary
        self.months = monthsWorked
    #Returns yearly pay by multiplying months worked and monthly salary
    def yearlyPay(self):
        return self.salary * self.months
    #Returns monthly salary
    def monthlySalary(self):
        return self.salary
    #Returns months worked
    def monthsWorked(self):
        return self.months

