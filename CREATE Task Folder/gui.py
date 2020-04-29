import pygame

from button import Button

def mainMenuGUI(rpg):
    #Button stuff
    rpg.startButton.width = 420
    rpg.startButton.height = 69
    rpg.startButton.text_color = (255, 255, 255)
    rpg.startButton.font = pygame.font.SysFont('arial', 20)
    rpg.startButton.prep()

    #Square stuff
    width = rpg.settings.screen_width
    height = rpg.settings.screen_height
    top = 0
    left = 0
    color = (255, 255, 255)
    rect = pygame.Rect(left, top, width, height)
    
    


#def GUIUpdate():


