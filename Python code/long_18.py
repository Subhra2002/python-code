class Employee:
    company = "Whatsapp"
    salary = 800

    # def getSalary(self,sal):
    #     self.__class__.salary = sal
    @classmethod
    def getSalary(cls,sal):
        cls.salary = sal



s = Employee()
print(s.salary)
s.getSalary(600)
print(s.salary)
print(Employee.salary)
