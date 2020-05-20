import pygame


class place():
    def __init__(self, placeName):
        self.name = placeName
        self.checkConstraint = True
        self.monsterList = []
        self.constraint = ""
        self.background = ""
    
    def starterVillage(self, rpg):
        rpg.playerConsole.showNextText(rpg, "???: Hello! Welcome to the town of Hogsmeade.", "It's a small village but we get by.", pygame.image.load("CREATE Task Folder\Image Assets\Images_Npc\mayor.png").convert_alpha())
        rpg.playerConsole.showNextText(rpg, "Narco: What is your name?"," ", pygame.image.load("CREATE Task Folder\Image Assets\Images_Npc\mayor.png").convert_alpha())
        #playerTyping = True
        #while playerTyping == True:
            #event = pygame.event.poll
            #letterPressed = pygame.key.get_pressed()
            #key = pygame.key.name(event.key)
            #if len(key) == 1:
                #if letterPressed[pygame.K_LSHIFT] or letterPressed[pygame.K_RSHIFT]:
                    #rpg.playerName += key.upper()
                #else:
                    #rpg.playerName += key
            #elif key == pygame.K_BACKSPACE:
                #string = string[:len(string)-1]
            #elif key == pygame.K_RETURN:
                #playerTyping = False
        #message = "Hello,",rpg.player.name,"!"
        #rpg.playerConsole.showNextText(rpg, message, " ", pygame.image.load("CREATE Task Folder\Image Assets\Images_Npc\mayor.png").convert_alpha())
        rpg.playerConsole.showNextText(rpg, "Narco: What class are you?", " ", pygame.image.load("CREATE Task Folder\Image Assets\Images_Npc\mayor.png").convert_alpha())
        rpg.choiceButtons.choice6.msg = "Thief"
        rpg.choiceButtons.choice5.msg = "Commoner"
        rpg.choiceButtons.choice4.msg = "Squire"
        rpg.choiceButtons.choice3.msg = "Apprentice"
        rpg.choiceButtons.choice2.msg = "Warrior"
        rpg.choiceButtons.choice1.msg = "Archer"
        rpg.choiceButtons.draw()
        if(rpg.choiceButtons.choice6.rect.collidepoint(rpg.mous_pos)):
            rpg.player.profession = "Thief"
        if(rpg.choiceButtons.choice5.rect.collidepoint(rpg.mous_pos)):
            rpg.player.profession = "Commoner"
        if(rpg.choiceButtons.choice4.rect.collidepoint(rpg.mous_pos)):
            rpg.player.profession = "Squire"
        if(rpg.choiceButtons.choice3.rect.collidepoint(rpg.mous_pos)):
            rpg.player.profession = "Apprentice"
        if(rpg.choiceButtons.choice2.rect.collidepoint(rpg.mous_pos)):
            rpg.player.profession = "Warrior"
        if(rpg.choiceButtons.choice1.rect.collidepoint(rpg.mous_pos)):
            rpg.player.profession = "Archer"
        rpg.playerConsole.showNextText(rpg, "Narco: That's great! I need your help though...", " ", pygame.image.load("CREATE Task Folder\Image Assets\Images_Npc\mayor.png").convert_alpha())
