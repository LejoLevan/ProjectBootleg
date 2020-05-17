import pygame
from gui import playerConsole, border
from main import RPG

class place():
    def __init__(self,placeName):
        self.name = placeName
        self.checkConstraint = True
        self.monsterList = []
        self.constraint = ""
        self.background = ""
        self.playerConsole = playerConsole(self)
        self.border = self.border(self)
    
#Prints the information about the location the player is in

#Checks if constraints to move on to the next area have been met
    def goToArea(self):
        if(self.checkConstraint == True):
            print("You went to",self.name)
        print("The monsters in this place are",self.monsterList)
        print(self.background)
        print("Good luck!")
        if(self.checkConstraint != 1):
            print("You cannot go to that place")
            print("You still haven't", self.constraint)