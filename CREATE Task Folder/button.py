import pygame.font

class Button:

    def __init__(self,rpg,msg):
        """Initialize button attributes."""
        self.screen = rpg.screen
        self.screen_rect = self.screen.get_rect()

        #Set the dimensions and properties of the button
        self.width, self.height = 200, 50
        self.button_color = (0, 255, 0)
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 48)
        