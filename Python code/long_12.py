class Programmer:
    company = "microsoft"

    def __init__(self , name , product):
        self.name = name
        self.product = product

    def getInfo(self):
        print(f"The name of the Programmer is {self.name} and he/she works in {self.product} ")



Kuku = Programmer("laxmi",'Skype')
Jyoti = Programmer("Jeeban",'Github')
Kuku.getInfo()
Jyoti.getInfo()