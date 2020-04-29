import pygame

def mainMenuGUI(rpg):
    #Button stuff
    rpg.startButton.width = 420
    rpg.startButton.height = 69
    rpg.startButton.text_color = (255, 255, 255)
    rpg.startButton.font = pygame.font.SysFont('arial', 20)
    rpg.startButton.border = 1
    rpg.startButton.prep()

    #Square stuff
    rpg.borderSquare.width = rpg.settings.screen_width
    rpg.borderSquare.height = rpg.settings.screen_height
    rpg.borderSquare.top = 0
    rpg.borderSquare.left = 0
    rpg.borderSquare.color = (255, 255, 255)
    rpg.borderSquare.border = 1
    rpg.borderSquare.prep()
    
    
    


#def GUIUpdate():


