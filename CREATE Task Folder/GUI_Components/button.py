"""File contains a button making class"""
import pygame.font

class Button:
    """Button making class"""
    def __init__(self, rpg, msg):
        """Initialize button attributes."""
        self.screen = rpg.screen
        self.screen_rect = self.screen.get_rect()

        #Set the dimensions and properties of the button
        self.width, self.height = 200, 50
        self.button_color = (0, 0, 0)
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 48)
        self.msg = msg
        
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center

        self._prep_msg()
    
    def prep(self):
        self.prepRect()
        self._prep_msg()

    def prepRect(self):
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center

    def _prep_msg(self):
        """Turn msg into a rendered image and center text on the button."""
        self.msg_image = self.font.render(self.msg, True, self.text_color, self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center
    
    def draw_button(self):
        """Draws button"""
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)
    