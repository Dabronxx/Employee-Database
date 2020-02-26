#Import Employee Class
from Employee import*
#Class is derived from the Employee class
class PartTimeFaculty(Employee):
    #Constructor that takes in id number, first and last name, and also the number of classes taught
    def __init__(self, id, fname, lname, numberOfClasses):
        Employee.__init__(self, id, fname, lname)
        self.classes = numberOfClasses
    #Returns yearly pay by multiplying the number of classes by 1000
    def yearlyPay(self):
        return self.classes * 1000
    #Returns classes taught
    def totalClasses(self):
        return self.classes