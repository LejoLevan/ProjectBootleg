import random
import pygame

from monster import monster
from GUI_Components.button import Button
from GUI_Components.square import square
from GUI_Components.image import image


class battle:
    def __init__(self, rpg, location):
        self.enemy = monster(rpg)
        self.background = image(rpg, "CREATE Task Folder\Image Assets\Transparent.png", "")
        self.background.left, self.background.top = 0, 0
        self.background.width, self.background.height = 1050, 660

        if location == "Village":
            enemyList = [self.enemy.goblin()]
            random.choice(enemyList)
            self.background.image = pygame.image.load('CREATE Task Folder\Image Assets\Battle_Images\Village Forest.png')
        
        self.enemyImage = image(rpg, self.enemy.image, "")
        self.enemyImage.left, self.enemyImage.top = 250, 220
        self.enemyImage.width, self.enemyImage.height = 550, 420
        self.enemyImage.transparent = True

        self.enemyInfo = Button(rpg, "{} - Level: {}".format(self.enemy.name, self.enemy.level))
        self.enemyInfo.width, self.enemyInfo.height = 550, 35
        self.enemyInfo.left, self.enemyInfo.top = 250, 80
        self.enemyInfo.clickable = False

        self.enemyHP = Button(rpg, "HP: {}/{}".format(self.enemy.hp, self.enemy.maxhp))
        self.enemyHP.width, self.enemyHP.height = 275, 35
        self.enemyHP.left, self.enemyHP.top = 250, 115
        self.enemyHP.transparent = True
        self.enemyHP.clickable = False

        self.enemyHPbar = Button(rpg, "HP: {}/{}".format(self.enemy.hp, self.enemy.maxhp))
        self.enemyHPbar.width, self.enemyHPbar.height = 275, 35
        self.enemyHPbar.left, self.enemyHPbar.top = 250, 115
        self.enemyHPbar.button_color = (200, 0, 0)
        self.enemyHPbar.text_color = (200, 0, 0)
        self.enemyHPbar.clickable = False

        self.enemyStamina = Button(rpg, "Stamina: {}/{}".format(self.enemy.stamina, self.enemy.stamina_max))
        self.enemyStamina.width, self.enemyStamina.height = 275, 35
        self.enemyStamina.left, self.enemyStamina.top = 525, 115
        self.enemyStamina.transparent = True
        self.enemyStamina.clickable = False

        self.enemyStaminaBar = Button(rpg, "Green")
        self.enemyStaminaBar.width, self.enemyStaminaBar.height = 275, 35
        self.enemyStaminaBar.left, self.enemyStaminaBar.top = 525, 115
        self.enemyStaminaBar.button_color = (0, 200, 0)
        self.enemyStaminaBar.text_color = (0, 200, 0)
        self.enemyStaminaBar.clickable = False

        self.enemyMana = Button(rpg, "Mana: {}/{}".format(self.enemy.mana, self.enemy.mana_max))
        self.enemyMana.width, self.enemyMana.height = 550, 35
        self.enemyMana.left, self.enemyMana.top = 250, 150
        self.enemyMana.transparent = True
        self.enemyMana.clickable = False

        self.enemyManaBar = Button(rpg, "Blue")
        self.enemyManaBar.width, self.enemyManaBar.height = 550, 35
        self.enemyManaBar.left, self.enemyManaBar.top = 250, 150
        self.enemyManaBar.button_color = (0, 0, 200)
        self.enemyManaBar.text_color = (0, 0, 200)
        self.enemyManaBar.clickable = False

        self.enemyStats = False
        self.combatLoop(rpg)

    def combatLoop(self, rpg):
        self.whoFirst
    
    def mouseEvents(self, mous_pos):
        if self.enemyImage.rect.collidepoint(mous_pos):
            if self.enemyStats == False:
                self.enemyStats = True
            else:
                self.enemyStats = False
    
    def update(self):
        self.enemyMana.msg = "Mana: {}/{}".format(self.enemy.mana, self.enemy.mana_max)
        try:
            self.enemyManaBar.width = 275 * ((self.enemy.mana/self.enemy.mana_max))
        except Exception:
            self.enemyManaBar.width = 0
            self.enemyMana.transparent = False

        self.enemyStamina.msg = "Stamina: {}/{}".format(self.enemy.stamina, self.enemy.stamina_max)
        try:
            self.enemyStaminaBar.width = 275 * ((self.enemy.stamina/self.enemy.stamina_max))
        except Exception:
            self.enemyStaminaBar.width = 0
            self.enemyStamina.transparent = False

        self.enemyHP.msg = "Stamina: {}/{}".format(self.enemy.hp, self.enemy.maxhp)
        try:
            self.enemyHPbar.width = 275 * ((self.enemy.hp/self.enemy.maxhp))
        except Exception:
            self.enemyHPbar.width = 0
            self.enemyHP.transparent = False



    def draw(self):
        self.update()
        self.background.draw()
        self.enemyImage.draw()
        if self.enemyStats == True:
            self.enemyInfo.draw()
            self.enemyHPbar.draw()
            self.enemyHP.draw()
            self.enemyStaminaBar.draw()
            self.enemyStamina.draw()
            self.enemyManaBar.draw()
            self.enemyMana.draw()

            