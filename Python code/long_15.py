# this Inheritance is a singel type Inheritance😁😁
class Employee:
    company = "Google"

    def showDetails(self):
        print("I am a Employee of Google company")


class Programmer(Employee):
    language = "Python"

    def getName(self):
        print(f"i am software devloper and work on {self.language}")

    def showDetails(self):
        print(f"I am a programmer of {self.company}")


e = Employee()
p = Programmer()
e.showDetails()
p.getName()
p.showDetails()
