"""main file, contains the main class"""

import sys

import pygame

from Save_Games.save_methods import playerLoad
from player import character
from button import Button
from settings import Settings
from image_template import Template #Y'all can probably ignore this entire class (I still need for stuff)
#from Quest_System.main_class_quest import QuestChecker (example of importing a file from a dif folder)

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
        self.game_active = False
        self.play_button = Button(self, "Play")
        self.player = character()

  
    def run_game(self):
        """Start the main loop for the game"""
        while True:
            self._check_events()
            if self.game_active:
                self.template.update()
                self.player.update()
            self._update_screen()

    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mous_pos = pygame.mouse.get_pos()
                self._check_mouseclick(mous_pos)
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def _check_mouseclick(self, mous_pos):
        if self.play_button.rect.collidepoint(mous_pos) and not self.game_active:
            self.game_active = True

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
        if not self.game_active:
            self.play_button.draw_button()
        pygame.display.flip()

if __name__ == '__main__':
    BOOTLEG = RPG()
    BOOTLEG.run_game()
