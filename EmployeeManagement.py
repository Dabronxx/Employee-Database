# Overall Plan:
# 1. Import all three derived Employee classes
# 2. In the constructor, initialize a new list of employees
# 3. Create a method that appends an employee object to the list
# 4. Create a method that removes an employee by referencing the employee's last name
# 5. Create a method that takes employee information, creates an employee object from that information, and then appends it to the list
# 6. Have six parameters where the last element is optional
# 7. Determine the employee type by the id number, ids < 100 are partTime, 100 < id <200 are salaried, and above that is hourly
# 8. Create a method that saves the information from each employee to a new database file in a neatly printed format
# 9. Create a method that loads a file and reads in all of the information, creates employee objects from the information and then adds it to the list
# 10. Be sure to skip any lines that do not contain information pertaining to an employee

#Import all three derived Employee classes
from PartTimeFaculty import*
from SalariedEmployee import*
from HourlyEmployee import*
class EmployeeManagement:
    #In the constructor, initialize a new list of employees
    def __init__(self):
        self.employeeList = []

    #Create a method that appends an employee object to the list
    def add(self, employee):
        self.employeeList.append(employee)

    #Create a method that removes an employee by referencing the employee's last name
    def remove(self, lname):
        for employee in self.employeeList:
            if lname == employee.getLastName():
                self.employeeList.remove(employee)

    #Create a method that takes employee information, creates an employee object from that information, and then appends it to the list
    #Have six parameters where the last element is optional
    def addEmployee(self, id, lname, fname, classesOrSalaryOrMonths, hourlyRateorSalary = 0):
        #Determine the employee type by the id number, ids < 100 are partTime, 100 < id <200 are salaried, and above that is hourly
        if id < 100:
            newEmployee = PartTimeFaculty(id, fname, lname, classesOrSalaryOrMonths)
        elif id < 200:
            newEmployee = SalariedEmployee(id, fname, lname, classesOrSalaryOrMonths, hourlyRateorSalary)
        else:
            newEmployee = HourlyEmployee(id, fname, lname, classesOrSalaryOrMonths, hourlyRateorSalary)
        self.add(newEmployee)

    #Create a method that saves the information from each employee to a new database file in a neatly printed format
    def save(self, fileName):
        self.outfile = open(fileName, 'w')
        print("ID#  Last Name  First Name Classes/Hours/Months Salary/Hourly-Rate Yearly Pay", file = self.outfile)
        print("—————————————————————————————————————————————————————————————————————————————", file = self.outfile)
        for item in self.employeeList:
            if item.id < 100:
                print("{0:4}".format(str(item.getID())), "{0:10}".format(item.getLastName()),
                      "{0:10}".format(item.getFirstName()), "{0:41}".format(str(item.totalClasses())), "${0:20}".format(str(item.yearlyPay())), file = self.outfile)
            elif item.id < 200:
                print("{0:4}".format(str(item.getID())), "{0:10}".format(item.getLastName()),
                      "{0:24}".format(item.getFirstName()), "{0:6}".format(str(item.monthsWorked())), "${0:19}".format(str(item.monthlySalary())),
                      "${0:10}".format(str(item.yearlyPay())), file = self.outfile)
            else:
                print("{0:4}".format(str(item.getID())), "{0:10}".format(item.getLastName()),
                      "{0:18}".format(item.getFirstName()), "{0:19}".format(str(item.hoursWorked())),
                      "${0:12}".format(str(item.hourlyRate())), "${0:10}".format(str(item.yearlyPay())), file=self.outfile)
        self.outfile.close()

    #Create a method that loads a file and reads in all of the information, creates employee objects from the information and then adds it to the list
    #Be sure to skip any lines that do not contain information
    def load(self, fileName):
        with open(fileName, 'r') as self.infile:
            for i in range(2):
                next(self.infile)
            for line in self.infile:
                information = line.split()
                if len(information) == 4:
                    id, lname, fname, classesOrSalaryOrHours = line.split()
                    self.addEmployee(int(id), lname, fname, int(classesOrSalaryOrHours))
                else:
                    id, lname, fname, classesOrSalaryOrHours, hourlyRate = line.split()
                    self.addEmployee(int(id), lname, fname, int(classesOrSalaryOrHours), int(hourlyRate))
        self.infile.close()

