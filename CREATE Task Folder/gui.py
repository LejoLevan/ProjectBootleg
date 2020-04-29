import pygame

def mainMenuGUI(rpg):
    #LoadButton Settings
    rpg.loadButton.width = 420
    rpg.loadButton.height = 69
    rpg.loadButton.text_color = (255, 255, 255)
    rpg.loadButton.font = pygame.font.SysFont('arial', 20)
    rpg.loadButton.border = 1
    rpg.loadButton.top = (rpg.settings.screen_height*.5) - (rpg.loadButton.height/2) + 75
    rpg.loadButton.left = (rpg.settings.screen_width*.5) - (rpg.loadButton.width/2)
    rpg.loadButton.prep()

    #OuterBorder
    rpg.borderSquare.width = rpg.settings.screen_width
    rpg.borderSquare.height = rpg.settings.screen_height
    rpg.borderSquare.top = 0
    rpg.borderSquare.left = 0
    rpg.borderSquare.color = (255, 255, 255)
    rpg.borderSquare.border = 1
    rpg.borderSquare.prep()
    
    #New game button
    rpg.newGameButton.width = 420
    rpg.newGameButton.height = 69
    rpg.newGameButton.text_color = (255, 255, 255)
    rpg.newGameButton.font = pygame.font.SysFont('arial', 20)
    rpg.newGameButton.border = 1
    rpg.newGameButton.top = (rpg.settings.screen_height*.5) - (rpg.newGameButton.height/2) 
    rpg.newGameButton.left = (rpg.settings.screen_width*.5) - (rpg.newGameButton.width/2)
    rpg.newGameButton.prep()
    
    #Quit Button
    rpg.quitButton.width = 420
    rpg.quitButton.height = 69
    rpg.quitButton.text_color = (255,255,255)
    rpg.quitButton.font = pygame.font.SysFont('arial', 20)
    rpg.quitButton.border = 1
    rpg.quitButton.top = (rpg.settings.screen_height*.5) - (rpg.quitButton.height/2) + 150
    rpg.quitButton.left = (rpg.settings.screen_width*.5) - (rpg.quitButton.width/2)
    rpg.quitButton.prep()

    #Project Logo
    rpg.logo.top = (rpg.settings.screen_height*.5) - (rpg.logo.height/2) - 200
    rpg.logo.left = (rpg.settings.screen_width*.5) - (rpg.logo.width/2)
    rpg.logo.prep()


def choiceButton(rpg,ypos,xpos):
    rpg.choice.width = 600
    rpg.choice.height = 80
    rpg.choice.text_color(255,255,255)
    rpg.choice.font = pygame.font.SysFont('arial',20)
    rpg.choice.border = 1
    rpg.choice.top = (rpg.settings.screen_height*.5) - (rpg.choice.height/2) + ypos
    rpg.choice.left = (rpg.settings.screen_width*.5) - (rpg.choice.width/2) + xpos
    rpg.choice.prep()