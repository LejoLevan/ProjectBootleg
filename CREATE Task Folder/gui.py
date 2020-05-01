import pygame

def mainMenuGUI(rpg):
    #LoadButton Settings
    rpg.loadButton.startDefault(rpg, 75, 0)
    
    #OuterBorder
    rpg.borderSquare.width = rpg.settings.screen_width
    rpg.borderSquare.height = rpg.settings.screen_height
    rpg.borderSquare.top = 0
    rpg.borderSquare.left = 0
    rpg.borderSquare.color = (255, 255, 255)
    rpg.borderSquare.border = 1
    rpg.borderSquare.prep()
    
    #New game button
    rpg.newGameButton.startDefault(rpg, 0 , 0)
    
    #Quit Button
    rpg.quitButton.startDefault(rpg, 150, 0)

    #Project Logo
    rpg.logo.top = (rpg.settings.screen_height*.5) - (rpg.logo.height/2) - 200
    rpg.logo.left = (rpg.settings.screen_width*.5) - (rpg.logo.width/2)

def createChoiceButton(rpg):
    rpg.choice1.choiceDefault(rpg, -375, 0)
    rpg.choice2.choiceDefault(rpg, -300, 0)
    rpg.choice3.choiceDefault(rpg, -225, 0)
    rpg.choice4.choiceDefault(rpg, -150, 0)
    rpg.choice5.choiceDefault(rpg, -75, 0)
    rpg.choice6.choiceDefault(rpg, 0, 0)