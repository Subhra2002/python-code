class Train:
    def __init__(self , name ,fare , seats):
        self.name = name
        self.fare = fare
        self.seats = seats

    def getStatus(self):
        print(f"the name of the train is {self.name}")
        print(f"the seats are avalilable is {self.seats}")
    def getInfo(self):
        print(f"the price of the ticket is {self.fare}")

    def bookTicket(self):
        if (self.seats > 0):
            print(f"Your ticket is booked🤗🤗 ! Your seats number is {self.seats}")
            self.seats = self.seats -1
        else:
            print("Sorry😥 the train is full ! Next time try faster")

Rajdhani = Train("Rajdhani express: 125609 ", 130, 0 )
Rajdhani.getStatus()
Rajdhani.getInfo()
Rajdhani.bookTicket()
Rajdhani.getStatus()