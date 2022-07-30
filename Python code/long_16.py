# This is a multiple Inheritance .......
class School:
    subject = "Math"
    

class College:
    course = "Science"
    rollNo = 20

    def upgradeRollno(self):
        self.rollNo = self.rollNo + 1

class University(School,College):
    branche = "Computer Science"
    

 

Subha = University()
Subha.upgradeRollno()
print(Subha.rollNo)
