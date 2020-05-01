import pygame
class image:
    def __init__(self, rpg, path):
        self.screen = rpg.screen
        self.settings = rpg.settings
        self.screen_rect = rpg.screen.get_rect()

        self.image = pygame.image.load(path)

        self.width, self.height = self.image.get_width(), self.image.get_height()
        self.left, self.top = 0, 0

        self.image = pygame.transform.scale(self.image, (self.width, self.height))

        self.rect = pygame.Rect(self.left, self.top, self.width, self.height)

    def draw(self):
        self.image = pygame.transform.scale(self.image, (self.width, self.height))
        self.rect = pygame.Rect(self.left, self.top, self.width, self.height)
        """Draw the template at its current location"""
        self.screen.blit(self.image, self.rect)