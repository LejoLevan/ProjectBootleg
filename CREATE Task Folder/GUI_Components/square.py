import pygame

class square:
    def __init__(self, rpg):
        self.screen = rpg.screen
        self.screen_rect = self.screen.get_rect()

        self.width, self.height = 200, 50
        self.left, self.top = 0, 0
        self.square_color = (255, 255, 255)
        self.border = 0

        self.rect = pygame.Rect(0, 0, self.width, self.height)
    
    def prep(self):
        self.rect = pygame.Rect(0, 0, self.width, self.height)

    def drawSquare(self):
        pygame.draw.rect(self.screen, self.square_color, self.rect, self.border)