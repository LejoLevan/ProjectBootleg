import pygame
class image:
    def __init__(self, rpg, path, msg):
        self.screen = rpg.screen
        self.settings = rpg.settings
        self.screen_rect = rpg.screen.get_rect()

        self.image = pygame.image.load(path)

        self.width, self.height = self.image.get_width(), self.image.get_height()
        self.left, self.top = 0, 0

        self.font = pygame.font.SysFont('arial', 20)
        self.msg = msg
        self.button_color = (0, 0, 0)
        self.text_color = (255, 255, 255)
        self.border = False
        self.clickable = False

        self.image = pygame.transform.scale(self.image, (self.width, self.height))

        self.rect = pygame.Rect(self.left, self.top, self.width, self.height)
        self._prep_msg()

    def _prep_msg(self):
        """Turn msg into a rendered image and center text on the button."""
        self.msg_image = self.font.render(self.msg, True, self.text_color, self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center
    
    def prep(self):
        self.prepRect()
        self._prep_msg()

    def prepRect(self):
        if self.border == True:
            pygame.draw.rect(self.screen, self.text_color, self.rect, 3)
        self.rect = pygame.Rect(self.left, self.top, self.width, self.height)

    def draw(self):
        if (self.clickable == True):
            if self.rect.collidepoint(pygame.mouse.get_pos()):
                self.button_color = (200, 200, 200)
            else:
                self.button_color = (0, 0, 0)
        self.image = pygame.transform.scale(self.image, (self.width, self.height))
        self.prep()
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.image, self.rect)
        if self.msg != "":
            self.screen.blit(self.msg_image, self.msg_image_rect)