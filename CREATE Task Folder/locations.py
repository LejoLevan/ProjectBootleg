import pygame


class place():
    def __init__(self, placeName, rpg):
        self.name = placeName
        self.checkConstraint = True
        self.monsterList = []
        self.constraint = ""
        self.background = ""
    
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

    def starterVillage(self, rpg):
        while(1 == 1):
            mous_pos = pygame.mouse.get_pos()
        rpg.playerConsole.showNextText("???: Hello! Welcome to the town of Hogsmeade.", "It's a small village but we get by.", pygame.image.load("CREATE Task Folder\Image Assets\Images_Npc\mayor.png").convert_alpha())
        continueCheck = True
        while(continueCheck == True):
            if rpg.borders.textSquare.rect.collidepoint(mous_pos):
                rpg.playerConsole.showNextText("Narco: What is your name?"," ", pygame.image.load("CREATE Task Folder\Image Assets\Images_Npc\mayor.png").convert_alpha())
                continueCheck = False
                player.name = input("Enter your name: ")
                message = "Hello,",player.name,"!"
                rpg.playerConsole.showNextText(message, " ", pygame.image.load("CREATE Task Folder\Image Assets\Images_Npc\mayor.png").convert_alpha())
            continueCheck = True
            while(continueCheck == True):
                if rpg.borders.textSquare.rect.collidepoint(mous_pos):
                    continueCheck = False
                    rpg.playerConsole.showNextText("Narco: What class are you?", " ", pygame.image.load("CREATE Task Folder\Image Assets\Images_Npc\mayor.png").convert_alpha())
                    rpg.choice6.msg = "Thief"
                    rpg.choice5.msg = "Commoner"
                    rpg.choice4.msg = "Squire"
                    rpg.choice3.msg = "Apprentice"
                    rpg.choice2.msg = "Warrior"
                    rpg.choice1.msg = "Archer"
                    if(rpg.choiceButtons.choice6.rect.collidepoint(mous_pos)):
                        player.profession = "Thief"
                    if(rpg.choiceButtons.choice5.rect.collidepoint(mous_pos)):
                        player.profession = "Commoner"
                    if(rpg.choiceButtons.choice4.rect.collidepoint(mous_pos)):
                        player.profession = "Squire"
                    if(rpg.choiceButtons.choice3.rect.collidepoint(mous_pos)):
                        player.profession = "Apprentice"
                    if(rpg.choiceButtons.choice2.rect.collidepoint(mous_pos)):
                        player.profession = "Warrior"
                    if(rpg.choiceButtons.choice1.rect.collidepoint(mous_pos)):
                        player.profession = "Archer"
                    while(continueCheck == True):
                        continueCheck = False
                        if(rpg.borders.textSquare.rect.collidepoint(mous_pos)):
                            rpg.playerConsole.showNextText("Narco: That's great! I need your help though...", " ", pygame.image.load("CREATE Task Folder\Image Assets\Images_Npc\mayor.png").convert_alpha())
                            