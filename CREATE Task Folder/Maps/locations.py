from main import player


class place():
    def __init__(self,name,constraint,monsterList,background):
        self.name = placeName
        self.checkConstraint = 0
        self.monsterList = []
        self.constraint = ""
        self.background = ""
    
#Prints the information about the location the player is in
    def placeInformation(self):
        print("You went to",self.name)
        print("The monsters in this place are",self.monsterList)
        print(self.background)
        print("Good luck!")

#Checks if constraints to move on to the next area have been met
    def goToArea(self):
        if(checkConstraint = 1):
            placeInformation(self)
        if(checkConstraint != 1):
            print("You cannot go to that place")
            print("You still haven't", constraint)