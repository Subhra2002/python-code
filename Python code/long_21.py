class Employee:
    company = "Google"

    def __init__(self,salary):
        self.salary = salary
        print(f"the salary is {self.salary}")

e = Employee(100)