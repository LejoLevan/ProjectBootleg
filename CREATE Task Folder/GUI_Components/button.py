"""File contains a button making class"""
import pygame.font

class Button:
    """Button making class"""
    def __init__(self, rpg, msg):
        """Initialize button attributes."""
        self.screen = rpg.screen

        #Set the dimensions and properties of the button
        self.border = True
        self.clickable = False
        self.width, self.height = 200, 50
        self.button_color = (0, 0, 0)
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 48)
        self.msg = msg
        self.top = (rpg.settings.screen_height) - (self.height/2)
        self.left = (rpg.settings.screen_width) - (self.width/2)
        self.rect = pygame.Rect(self.left, self.top, self.width, self.height)

        self._prep_msg()

    def startDefault (self, topDif, leftDif):
        self.border = True
        self.clickable = True
        self.width, self.height = 800, 70
        self.font = pygame.font.SysFont('arial', 20)
        self.top = self.top + topDif
        self.left = self.top + leftDif

    def choiceDefault(self, topDif, leftDif):
        self.border = True
        self.clickable = True
        self.width, self.height = 800, 70
        self.font = pygame.font.SysFont('arial', 20)
        self.top = self.top + topDif
        self.left = self.top + leftDif

    
    def prep(self):
        self.prepRect()
        self._prep_msg()

    def prepRect(self):
        self.rect = pygame.Rect(self.left, self.top, self.width, self.height)

    def _prep_msg(self):
        """Turn msg into a rendered image and center text on the button."""
        self.msg_image = self.font.render(self.msg, True, self.text_color, self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center
    
    def update(self):
        if (self.clickable == True):
            if self.rect.collidepoint(pygame.mouse.get_pos()):
                self.button_color = (200, 200, 200)
            else:
                self.button_color = (0, 0, 0)
        self.prep()
            

    def draw_button(self):
        """Draws button"""
        if self.border == True:
            pygame.draw.rect(self.screen, self.text_color, self.rect, 1)
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)
    