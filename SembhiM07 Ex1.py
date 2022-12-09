##name Navdeep Sembhi
##class Sdev 140
##profname Lee Wolfe
##date July 27 2022
##Variables:
## on mail
## custNum
##customer details
## telephone


# Person class with data attributes person’s name, address, and telephone number
class Person():
    def __init__(self,name,address,telephone):
        self.name = name
        self.address = address
        self.telephone = telephone
        
# Customer class, a subclass of Person class with data attributes customer number
# and boolean data attribute indicating whether the customer wishes to be on a mailing list
class Customer(Person):
    def __init__(self,name,address,telephone,custNum,onMail):
        self.custNum = custNum
        self.onMail = onMail
        super().__init__(name,address,telephone)
        
    def printDetails(self):
        print("Customer details -")
        print("Name: " + self.name)
        print("Address: " + self.address)
        print("Telephone: " + self.telephone)
        print("Number: " + self.custNum)
        print("On mailing list: " + str(self.onMail))
        

# Creating an instance of Customer class with name- Jhon, address- US, 
# telephone- 5556-1023, Customer number- C1022 and on mailing list- True
c = Customer("Navdeep Sembhi","INDIANA","(317) 840-2447","#5",True)

# Printing Customer details
c.printDetails()
