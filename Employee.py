class Employee:
    #Constructor that takes in id number, first and last name
    def __init__(self, id, fname, lname):
        self.fname = fname
        self.lname = lname
        self.id = id
    #Abstract method for the yearly pay calculation
    def yearlyPay(self):
        raise NotImplementedError("Subclass must implement abstract method")
    #Returns first name
    def getFirstName(self):
        return self.fname
    #Returns last name
    def getLastName(self):
        return self.lname
    #Returns ID number
    def getID(self):
        return self.id
