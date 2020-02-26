#Import Employee Class
from Employee import*
#Class is derived from the Employee class
class HourlyEmployee(Employee):
    # Constructor that takes in id number, first and last name, hours worked and hourly rate
    def __init__(self, id, fname, lname, hoursWorked, hourlyRate):
        Employee.__init__(self, id, fname, lname)
        self.hours = hoursWorked
        self.rate = hourlyRate
    #Returns yearly pay by multiplying the hours worked by the hourly rate
    def yearlyPay(self):
        return self.hours * self.rate
    #Returns hours worked
    def hoursWorked(self):
        return self.hours
    #Returns hourly rate
    def hourlyRate(self):
        return self.rate