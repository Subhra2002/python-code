
class Employee:
    company = "Google"

    def __init__(self , name , salary):
         self.name = name 
         self.salary = salary
         print(f"The real name of the Employee is {self.name}")
         print(f"The real salary of the Employee is {self.salary}")
        
    @staticmethod
    def getBouns():
            print(f"Diwali bouns is 2000 gift voucher for all")



    def greet(self,branch):
        print(f"This emplyoee working in {branch} in the {self.company}")


Subhra = Employee("pradeep","50k")
Priti= Employee("Priti","80k")
Subhra.getBouns()
Subhra.greet("Youtube")
Priti.getBouns()
