"""main file, contains the main class"""

import sys

import pygame

from gui import mainMenu, choiceButtons, statSheet, borders, swapButton, profilePic, playerConsole, combatGUI
from inventory import Inventory
from Save_Games.save_methods import playerLoad, questLoad, playerSave, questSave
from Quests.quest_class import QuestChecker
from player import character
from settings import Settings
from image_template import Template #Y'all can probably ignore this entire class (I still need for stuff)
from combat import battle
class RPG:
    """Overall class to mangage game assets and behavior."""
    def __init__(self):
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode([self.settings.screen_width, self.settings.screen_height], pygame.FULLSCREEN)
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height
        pygame.display.set_caption("Project Bootleg")

        self.template = Template(self)
        self.game_active = False
        self.battle_active = False

        self.player = character()
        self.quests = QuestChecker()
        
        self.mainMenu = mainMenu(self)
        self.borders = borders(self)
        self.statSheet = statSheet(self)
        self.choiceButtons = choiceButtons(self)
        self.swapButton = swapButton(self)
        self.profilePic = profilePic(self)
        self.playerConsole = playerConsole(self)
        self.Inventory = Inventory(self)
        self.playerConsole.newSlot = 0
        self.combatGUI = combatGUI(self)

    def loadData(self):
        try:
            self.player.loadStats(playerLoad())
            self.quests.loadQuest(questLoad())
            self.game_active = True
        except Exception:
            self.game_active = True
    
    def saveData(self):
        playerSave(self.player)
        questSave(self.quests)
        
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
        if self.choiceButtons.choice6.rect.collidepoint(mous_pos) and self.game_active:
            self.playerConsole.showNextText("None", "", pygame.image.load("CREATE Task Folder\Image Assets\Enemy_images\Goblin Miner.png").convert_alpha())
        if self.mainMenu.loadButton.rect.collidepoint(mous_pos) and not self.game_active:
            self.battle = battle(self, "Village")
            self.battle_active = True
            self.loadData()
        if self.mainMenu.newGameButton.rect.collidepoint(mous_pos) and not self.game_active:
            self.game_active = True
            self.playerConsole.resetConsole()
            self.playerConsole.showNextText("???: Hello! Welcome to the town of Hogsmeade.", "It's a small village but we get by.", pygame.image.load("CREATE Task Folder\Image Assets\GUI_images\WeaponTag.png").convert_alpha())
        if self.mainMenu.quitButton.rect.collidepoint(mous_pos) and not self.game_active:
            sys.exit()
        if self.game_active:
            if self.battle_active == True:
                self.battle.mouseEvents(mous_pos)
            self.swapButton.mouseEvents(mous_pos)
            self.Inventory.mouseEvents(self, mous_pos)
        
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
        if not self.game_active:
            self.mainMenu.draw()
            self.borders.borderSquare.draw()
        else:
            self.template.blitme()
            self.swapButton.draw()
            self.profilePic.draw()
            self.choiceButtons.draw()
            self.playerConsole.drawConsole()
            self.statSheet.showStats(self)
            if self.swapButton.inventoryShow == True:
                self.Inventory.draw(self)
            if self.battle_active == True:
                self.combatGUI.draw()
                self.battle.draw()
            else:
                self.choiceButtons.draw()
            self.borders.draw()
        pygame.display.flip()

if __name__ == '__main__':
    BOOTLEG = RPG()
    BOOTLEG.run_game()
