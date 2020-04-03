import sys

import pygame

from settings import Settings
from Adding_Images_Template import Template

class RPG:
    """Overall class to mangage game assets and behavior."""
    def __init__(self):
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height
        pygame.display.set_caption("Project Bootleg")
        self.template = Template(self)

    def run_game(self):
        """Start the main loop for the game"""
        while True:
            self._check_events()
            self.template.update()
            self._update_screen()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def _check_keydown_events(self, event):
        if event.key == pygame.K_RIGHT:
            self.template.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.template.moving_left = True
        elif event.key == pygame.K_q:
            sys.exit()

    def _check_keyup_events(self, event):
        if event.key == pygame.K_RIGHT:
            self.template.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.template.moving_left = False

    def _update_screen(self):
        self.screen.fill(self.settings.bg_color)
        self.template.blitme()
        pygame.display.flip()

if __name__ == '__main__':
    BOOTLEG = RPG()
    BOOTLEG.run_game()
