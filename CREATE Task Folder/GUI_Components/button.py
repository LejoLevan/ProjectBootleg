"""File contains a button making class"""
import pygame.font

class Button:
    """Button making class"""
    def __init__(self, rpg, msg):
        """Initialize button attributes."""
        self.screen = rpg.screen

        #Set the dimensions and properties of the button
        self.border = True
        self.clickable = True
        self.width, self.height = 200, 50
        self.button_color = (0, 0, 0)
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont('arial', 20)
        self.msg = msg
        self.top = (rpg.settings.screen_height*.5) - (self.height/2)
        self.left = (rpg.settings.screen_width*.5) - (self.width/2)
        self.rect = pygame.Rect(self.left, self.top, self.width, self.height)

        self._prep_msg()

    def startDefault (self, rpg, topDif, leftDif):
        self.width, self.height = 420, 69
        self.top = (rpg.settings.screen_height*.5) - (self.height/2) + topDif
        self.left = (rpg.settings.screen_width*.5) - (self.width/2) + leftDif

    def choiceDefault(self, rpg, topDif, leftDif):
        self.width, self.height = 800, 70
        self.font = pygame.font.SysFont('arial', 20)
        self.top = (rpg.settings.screen_height*.5) - (self.height/2) + topDif
        self.left = (rpg.settings.screen_width*.5) - (self.width/2) + leftDif


    def statDefault(self, rpg, topDif, leftDif):
        self.width, self.height = 400, 69
        self.font = pygame.font.SysFont('arial', 20)
        self.top = (rpg.settings.screen_height*.5) - (self.height/2) + topDif
        self.left = (rpg.settings.screen_width*.5) - (self.width/2) + leftDif
        self.clickable = False
        self.border = True
        
    
    def notifacationDefault(self, rpg, topDif, leftDif):
        self.width, self.height = self.font.size(self.msg)
        self.font = pygame.font.SysFont('arial', 20)
        self.top = (rpg.settings.screen_height*.5) - (self.height/2) + topDif
        self.left = (rpg.settings.screen_width*.5) - (self.height/2) + leftDif
        self.clickable = False
    
    def prep(self):
        self.prepRect()
        self._prep_msg()

    def prepRect(self):
        if self.border == True:
            pygame.draw.rect(self.screen, self.text_color, self.rect, 3)
        self.rect = pygame.Rect(self.left, self.top, self.width, self.height)

    def _prep_msg(self):
        """Turn msg into a rendered image and center text on the button."""
        self.msg_image = self.font.render(self.msg, True, self.text_color, self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw(self):
        """Draws button"""
        if (self.clickable == True):
            if self.rect.collidepoint(pygame.mouse.get_pos()):
                self.button_color = (200, 200, 200)
            else:
                self.button_color = (0, 0, 0)
        self.prep()
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)
    