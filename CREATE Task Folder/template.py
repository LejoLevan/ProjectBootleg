"""this is a template file that you reference when you want to add images"""

import pygame

class Template:
    """A class to manage the image"""
    def __init__(self, rpg):
        self.screen = rpg.screen
        self.settings = rpg.settings
        self.screen_rect = rpg.screen.get_rect()

        self.image = pygame.image.load('CREATE Task Folder\Images\Capture (1).png')#pylint: disable = anomalous-backslash-in-string
        self.rect = self.image.get_rect()

        self.rect.midbottom = self.screen_rect.midbottom

        self.x = float(self.rect.x)#pylint: disable = invalid-name

        # Movement Flags
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """Update the image's position based on the movement flag"""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.template_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.template_speed
        self.rect.x = self.x

    def blitme(self):
        """Draw the template at its current location"""
        self.screen.blit(self.image, self.rect)
