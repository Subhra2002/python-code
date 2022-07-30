class GrandFather:
    age = 78
    passion = "Writer"

    def getInfo(self):
        print('I am a Writer and i love to read Books...💚💛💛')

class Father(GrandFather):
    age = 48
    passion = "Traveling"

    def getInfo(self):
        super().getInfo()
        print("I am a Goverment worker and i love tea....🧡❤")

class Son(Father):
    age = 18
    passion = "Cricket"

    def getInfo(self):
        super().getInfo()
        print("i am a student and i love to paly Cricketer")

s = Son()
s.getInfo()


g = GrandFather()
g.getInfo()


f = Father()
f.getInfo()



