import pygame

class square:
    def __init__(self, rpg):
        self.screen = rpg.screen
        self.screen_rect = self.screen.get_rect()

        self.width = 1920
        self.height = 1080
        self.left, self.top = 0, 0
        self.square_color = (255, 255, 255)
        self.border = 1

        self.rect = pygame.Rect(self.left, self.top, self.width, self.height)
    
    def draw(self):
        self.rect = pygame.Rect(self.left, self.top, self.width, self.height)
        pygame.draw.rect(self.screen, self.square_color, self.rect, self.border)
    