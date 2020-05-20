import pygame

from GUI_Components.button import Button
from GUI_Components.square import square
from GUI_Components.image import image
from monster import monster


class combatGUI:
    def __init__(self, rpg):
        self.playerIcon = image(rpg, rpg.player.icon, rpg.player.name)#pylint: disable = anomalous-backslash-in-string
        self.playerIcon.iconDefault(rpg, -315)
        self.playerSquare = square(rpg)
        self.playerSquare.combatDefault(rpg, -315)
        self.playerAttack = Button(rpg, "Attack")
        self.playerAttack.combatDefault(rpg, -367.5, 0)
        self.playerDefend = Button(rpg, "Defend")
        self.playerDefend.combatDefault(rpg, -367.5, 205)
        self.playerRest = Button(rpg, "Rest")
        self.playerRest.combatDefault(rpg, -315, 0)
        self.playerUse = Button(rpg, "Use Item")
        self.playerUse.combatDefault(rpg, -315, 205)

        self.equipped_allies = rpg.player.equipped_allies
        
        try:
            if self.equipped_allies[0]:
                self.ally1Icon = image(rpg, rpg.player.equipped_allies[0].icon, rpg.player.equipped_allies[0].name)
                self.ally1Icon.iconDefault(rpg, -210)
                self.ally1Square = square(rpg)
                self.ally1Square.combatDefault(rpg, -210)
                self.ally1Attack = Button(rpg, "Attack")
                self.ally1Attack.combatDefault(rpg, -262.5, 0)
                self.ally1Defend = Button(rpg, "Defend")
                self.ally1Defend.combatDefault(rpg, -262.5, 205)
                self.ally1Rest = Button(rpg, "Rest")
                self.ally1Rest.combatDefault(rpg, -210, 0)
                self.ally1Use = Button(rpg, "Use Item")
                self.ally1Use.combatDefault(rpg, -210, 205)
                
            if self.equipped_allies[1]:
                self.ally2Icon = image(rpg, rpg.player.equipped_allies[1].icon, rpg.player.equipped_allies[1].name)
                self.ally2Icon.iconDefault(rpg, -105)
                self.ally2Square = square(rpg)
                self.ally2Square.combatDefault(rpg, -105)
                self.ally2Attack = Button(rpg, "Attack")
                self.ally2Attack.combatDefault(rpg, -157.5, 0)
                self.ally2Defend = Button(rpg, "Defend")
                self.ally2Defend.combatDefault(rpg, -157.5, 205)
                self.ally2Rest = Button(rpg, "Rest")
                self.ally2Rest.combatDefault(rpg, -105, 0)
                self.ally2Use = Button(rpg, "Use Item")
                self.ally2Use.combatDefault(rpg, -105, 205)
            
            if self.equipped_allies[2]:
                self.ally3Icon = image(rpg, rpg.player.equipped_allies[2].icon, rpg.player.equipped_allies[2].name)
                self.ally3Icon.iconDefault(rpg, 0)
                self.ally3Square = square(rpg)
                self.ally3Square.combatDefault(rpg, 0)
                self.ally3Attack = Button(rpg, "Attack")
                self.ally3Attack.combatDefault(rpg, -52.5, 0)
                self.ally3Defend = Button(rpg, "Defend")
                self.ally3Defend.combatDefault(rpg, -52.5, 205)
                self.ally3Rest = Button(rpg, "Rest")
                self.ally3Rest.combatDefault(rpg, 0, 0)
                self.ally3Use = Button(rpg, "Use Item")
                self.ally3Use.combatDefault(rpg, 0, 205)
        except:
            pass
        
        self.background = image(rpg, "CREATE Task Folder\Image Assets\Transparent.png", "")
        self.background.left, self.background.top = 0, 0
        self.background.width, self.background.height = 1050, 660

        self.enemy = monster(rpg)
        self.enemy.goblin()
        
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

        self.enemyHPbar = Button(rpg, "")
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

        self.enemyStaminaBar = Button(rpg, "")
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

        self.enemyManaBar = Button(rpg, "")
        self.enemyManaBar.width, self.enemyManaBar.height = 550, 35
        self.enemyManaBar.left, self.enemyManaBar.top = 250, 150
        self.enemyManaBar.button_color = (0, 0, 200)
        self.enemyManaBar.text_color = (0, 0, 200)
        self.enemyManaBar.clickable = False

        self.enemyStats = True
        self.attack = False
        self.defend = False
        self.rest = False
        self.use = False
        self.battleOver = False
        self.increaseDefend = False
        

    def mouseEvents(self, mous_pos):
        if self.enemyImage.rect.collidepoint(mous_pos):
            if self.enemyStats == False:
                self.enemyStats = True
            else:
                self.enemyStats = False
        if self.playerAttack.rect.collidepoint(mous_pos):
            self.attack = True
        if self.playerDefend.rect.collidepoint(mous_pos):
            self.defend = True
        if self.playerRest.rect.collidepoint(mous_pos):
            self.rest = True
        if self.playerUse.rect.collidepoint(mous_pos):
            self.use = True

    
    def update(self):
        self.enemyMana.msg = "Mana: {}/{}".format(self.enemy.mana, self.enemy.mana_max)
        try:
            if self.enemy.mana > 0:
                self.enemyManaBar.width = 275 * ((self.enemy.mana/self.enemy.mana_max))
            else:
                self.enemyMana.msg = "Mana: 0/{}".format(self.enemy.mana_max)
                self.enemyManaBar.width = 0
                self.enemyMana.transparent = False
        except Exception:
            self.enemyManaBar.width = 0
            self.enemyMana.transparent = False

        self.enemyStamina.msg = "Stamina: {}/{}".format(self.enemy.stamina, self.enemy.stamina_max)
        try:
            if self.enemy.stamina > 0:
                self.enemyStaminaBar.width = 275 * ((self.enemy.stamina/self.enemy.stamina_max))
            else:
                self.enemyStamina.msg = "Stamina: 0/{}".format(self.enemy.stamina_max)
                self.enemyStaminaBar.width = 0
                self.enemyStamina.transparent = False
        except Exception:
            self.enemyStaminaBar.width = 0
            self.enemyStamina.transparent = False

        self.enemyHP.msg = "HP: {}/{}".format(self.enemy.hp, self.enemy.maxhp)
        try:
            if self.enemy.hp > 0:
                self.enemyHPbar.width = 275 * ((self.enemy.hp/self.enemy.maxhp))
            else:
                self.enemyHP.msg = "HP: 0/{}".format(self.enemy.maxhp)
                self.enemyHPbar.width = 0
                self.enemyHP.transparent = False
        except Exception:
            self.enemyHPbar.width = 0
            self.enemyHP.transparent = False
        
        self.enemyInfo.msg = "{} - Level: {}".format(self.enemy.name, self.enemy.level)
        self.enemyImage.image = pygame.image.load(self.enemy.image)
        

    def draw(self):
        self.update()
        self.background.draw()
        self.enemyImage.draw()
        self.playerIcon.draw()
        self.playerAttack.draw()
        self.playerDefend.draw()
        self.playerRest.draw()
        self.playerUse.draw()
        self.playerSquare.draw()
        try:    
            if self.equipped_allies[0]: 
                self.ally1Attack.draw()
                self.ally1Defend.draw()
                self.ally1Rest.draw()
                self.ally1Use.draw()
                self.ally1Square.draw()

            if self.equipped_allies[1]:
                self.ally2Attack.draw()
                self.ally2Defend.draw()
                self.ally2Rest.draw()
                self.ally2Use.draw()          
                self.ally2Square.draw()

            if self.equipped_allies[2]:
                self.ally3Attack.draw()
                self.ally3Defend.draw()
                self.ally3Rest.draw()
                self.ally3Use.draw()          
                self.ally3Square.draw()
        except:
            pass
        
        if self.enemyStats == True:
            self.enemyInfo.draw()
            self.enemyHPbar.draw()
            self.enemyHP.draw()
            self.enemyStaminaBar.draw()
            self.enemyStamina.draw()
            self.enemyManaBar.draw()
            self.enemyMana.draw()