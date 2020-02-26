# Programmer:    Branko Andrews
# Date:          Dec. 15, 2016
#
# Problem Statement: You are creating a new Mira Costa Employee Management system.  There are 3 types of employees:
# Parttime Faculty, Salary(include fulltime Faculty), and Hourly.  You need to create a generic employee which holds
# the employees first and last name, and their id.  The parttime faculty member is paid a set amount(say 1000 per class)
# for each class they teach.  The salary employee is paid a monthly salary and the hourly employee is paid based on the
# number of hours work multiplied by their hourly rate.
# The management system should allow you to enter a new employee, remove an existing employee, save the existing employee
# database to a file, load an existing employee database file, and calculate the monthly paychecks for each employee.

# Overall Plan:
# 1. Import Employee Management
# 2. Create a new EmployeeManagement Object
# 3. Load the database onto the object
# 4. Create and add three new employee objects to the Employee Management object
# 5. Remove an employee currently in the database by last name
# 6. Save the new database


#Import Employee Management
from EmployeeManagement import*
def main():
    #Create a new EmployeeManagement Object
    directory = EmployeeManagement()

    #Load the database onto the object
    directory.load("database.txt")

    #Create and add three new employee objects to the Employee Management object
    tom = PartTimeFaculty(32, "Tom", "Harkins", 41)

    directory.add(tom)

    phil = SalariedEmployee(137, "Phil", "Adams", 10, 7400)

    directory.add(phil)

    directory.addEmployee(258, "Frank", "Thomas", 2740, 23)
    #Remove an employee currently in the database by last name
    directory.remove("Johnson")
    #Save the new database
    directory.save("updated_database.txt")

main()