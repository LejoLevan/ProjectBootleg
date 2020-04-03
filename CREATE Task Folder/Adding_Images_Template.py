import pygame

class Template:
    """A class to manage the image"""
    def __init__(self, rpg):
        self.screen = rpg.screen
        self.settings = rpg.settings
        self.screen_rect = rpg.screen.get_rect()

        self.image = pygame.image.load('images/Capture(1).png')
        self.rect = self.image.get_rect()

        self.rect.midbottom = self.screen_rect.midbottom

        self.x = float(self.rect.x)

        # Movement Flags
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """Update the image's position based on the movement flag"""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.rect.x += self.settings.template.speed
        if self.moving_left and self.rect.left > 0:
            self.rect.x -= self.settings.template.speed
        self.rect.x = self.x

    def blitme(self):
        """Draw the ship at its current location"""
        self.screen.blit(self.image, self.rect)
