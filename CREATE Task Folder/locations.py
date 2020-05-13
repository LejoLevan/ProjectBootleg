from gui import playerConsole

class place():
    def __init__(self,placeName):
        self.name = placeName
        self.checkConstraint = 0
        self.monsterList = []
        self.constraint = ""
        self.background = ""
        self.playerConsole = playerConsole(self)
    
#Prints the information about the location the player is in

#Checks if constraints to move on to the next area have been met
    def goToArea(self):
        if(self.checkConstraint == 1):
            print("You went to",self.name)
        print("The monsters in this place are",self.monsterList)
        print(self.background)
        print("Good luck!")
        if(self.checkConstraint != 1):
            print("You cannot go to that place")
            print("You still haven't", self.constraint)

    def startVillage(self):
        self.playerConsole.showNextText("Hello! Welcome to the town of Hogsmeade.", "It's a small village but we get by.")
        