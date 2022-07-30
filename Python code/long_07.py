class RailwayForm:
    formType = "RailwayForm"

    def PrintData(self):
        print(f"Name of the passenger is {self.name}")
        print(f"Name of the train is {self.train}")
rajveer = RailwayForm()
rajveer.name = "Raj Kumar Rao "
rajveer.train = "Rajdhani Express"

subhraApplication = RailwayForm()
subhraApplication.name = "SubhraPradeep"
subhraApplication.train = "Jana satabdhi"

subhraApplication.PrintData()
rajveer.PrintData()