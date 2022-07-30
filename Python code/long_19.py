
class Employee:
    salary = 500
    salaryBouns = 200
   
    

    @property
    def totalSalary(self):
        return self.salary + self.salaryBouns


    @totalSalary.setter
    def totalSalary(self, value ):
        self.salaryBouns = value - self.salary




s = Employee()
print(s.totalSalary)
s.totalSalary = 800
print(s.salary)
print(s.salaryBouns)

