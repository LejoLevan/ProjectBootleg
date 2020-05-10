import pygame
class image:
    def __init__(self, rpg, path, msg):
        self.screen = rpg.screen
        self.image = pygame.image.load(path).convert_alpha()

        self.width, self.height = self.image.get_width(), self.image.get_height()
        self.left, self.top = 0, 0

        self.font = pygame.font.SysFont('arial', 20)
        self.msg = msg
        self.button_color = (0, 0, 0)
        self.text_color = (255, 255, 255)
        self.border = False
        self.clickable = False
        self.textMidBottom = False
        self.transparent = False

        self.image = pygame.transform.scale(self.image, (self.width, self.height))
        self.rect = pygame.Rect(self.left, self.top, self.width, self.height)
        self._prep_msg()

    def tagDefault(self, rpg, leftDif):
        self.width, self.height = 180, 60
        self.font = pygame.font.SysFont('arial', 15)
        self.top = rpg.settings.screen_height - 420
        self.left = 0 + leftDif
        self.border = True
        self.clickable = True

    def iconDefault(self, rpg, topDif):
        self.width, self.height = 140, 105
        self.top = (rpg.settings.screen_height - self.height) + topDif
        self.left = rpg.settings.screen_width - 550
        self.font.set_bold(True)
        self.textMidBottom = True
    
    def inventoryDefault(self, rpg, topDif, leftDif):
        self.width, self.height = 100, 60
        self.top = rpg.settings.screen_height + topDif
        self.left = 0 + leftDif
        self.transparent = True

    def _prep_msg(self):
        """Turn msg into a rendered image and center text on the button."""
        self.msg_image = self.font.render(self.msg, True, self.text_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center
        if self.textMidBottom == True:
            self.msg_image_rect.midbottom = self.rect.midbottom
    
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
        self.image = pygame.transform.scale(self.image, (self.width, self.height)).convert_alpha()
        self.prep()
        if self.transparent == False:
            self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.image, self.rect)
        if self.msg != "":
            self.screen.blit(self.msg_image, self.msg_image_rect)