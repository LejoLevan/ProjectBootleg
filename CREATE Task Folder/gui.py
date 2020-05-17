import pygame

from GUI_Components.button import Button
from GUI_Components.square import square
from GUI_Components.image import image

class mainMenu():
    def __init__(self, rpg):
        #LoadButton Settings
        self.loadButton = Button(rpg, "Load")
        self.loadButton.startDefault(rpg, 75, 0)
          
        #New game button
        self.newGameButton = Button(rpg, "New Game")
        self.newGameButton.startDefault(rpg, 0, 0)
        
        #Quit Button
        self.quitButton = Button(rpg, "Quit")
        self.quitButton.startDefault(rpg, 150, 0)

        #Project Logo
        self.logo = image(rpg, 'CREATE Task Folder\Image Assets\GUI_images\ProjectLogo.png', "")#pylint: disable = anomalous-backslash-in-string
        self.logo.top = (rpg.settings.screen_height*.5) - (self.logo.height/2) - 200
        self.logo.left = (rpg.settings.screen_width*.5) - (self.logo.width/2)

    def draw(self):
        self.loadButton.draw()

        self.newGameButton.draw()

        self.quitButton.draw()

        self.logo.draw()

class choiceButtons():
    def __init__(self, rpg):
        self.choice1 = Button(rpg, "")
        self.choice1.choiceDefault(rpg, 0)
        
        self.choice2 = Button(rpg, "")
        self.choice2.choiceDefault(rpg, -70)
        
        self.choice3 = Button(rpg, "")
        self.choice3.choiceDefault(rpg, -140)
        
        self.choice4 = Button(rpg, "")
        self.choice4.choiceDefault(rpg, -210)
        
        self.choice5 = Button(rpg, "")
        self.choice5.choiceDefault(rpg, -280)
        
        self.choice6 = Button(rpg, "")
        self.choice6.choiceDefault(rpg, -350)

    def draw(self):
        self.choice1.draw()

        self.choice2.draw()

        self.choice3.draw()

        self.choice4.draw()

        self.choice5.draw()

        self.choice6.draw()

    def editChoices(self, choice1Text, choice2Text, choice3Text, choice4Text, choice5Text, choice6Text):
        self.choice1.msg = choice1Text
        self.choice2.msg = choice2Text
        self.choice3.msg = choice3Text
        self.choice4.msg = choice4Text
        self.choice5.msg = choice5Text
        self.choice6.msg = choice6Text

    def mouseEvents(self, rpg, mous_pos):
        if self.choice1.rect.collidepoint(mous_pos):
            rpg.playerConsole.newSlot = 1
            rpg.playerConsole.showNextText("", "No")
            print("hi")
            rpg.playerConsole.newSlot = 0

class statSheet():
    def __init__(self, rpg):
        self.hpStat = Button(rpg, "HP: {}/{}".format(rpg.player.hp, rpg.player.maxhp))
        self.hpStat.statDefault(rpg, -420, 0)

        self.stamStat = Button(rpg, "Stamina: {}/{}".format(rpg.player.stamina, rpg.player.stamina_max))
        self.stamStat.statDefault(rpg, -350, 0)

        self.manaStat = Button(rpg, "Mana: {}/{}".format(rpg.player.mana, rpg.player.mana_max))
        self.manaStat.statDefault(rpg, -280, 0)

        self.speedStat = Button(rpg, "Speed: {}".format(rpg.player.speed))
        self.speedStat.statDefault(rpg, -210, 0)

        self.physAtckStat = Button(rpg, "Physical Attack: {}".format(rpg.player.physical_attack))
        self.physAtckStat.statDefault(rpg, -140, 0)

        self.magicAtckStat = Button(rpg,  "Magic Attack: {}".format(rpg.player.magic_attack))
        self.magicAtckStat.statDefault(rpg, -70, 0)
        
        self.physDefStat = Button(rpg, "Physical Defense: {}".format(rpg.player.physical_defense))
        self.physDefStat.statDefault(rpg, -420, 350)

        self.magicDefStat = Button(rpg, "Magic Defense: {}".format(rpg.player.magic_defense))
        self.magicDefStat.statDefault(rpg, -350, 350)

        self.fireResist = Button(rpg, "Fire Resistance: {}".format(rpg.player.fire_resist))
        self.fireResist.statDefault(rpg, -280, 350)

        self.poisonResist = Button(rpg, "Poison Resistance: {}".format(rpg.player.poison_resist))
        self.poisonResist.statDefault(rpg, -210, 350)

        self.waterResist = Button(rpg, "Water Resistance: {}".format(rpg.player.water_resist))
        self.waterResist.statDefault(rpg, -140, 350)

        self.earthResist = Button(rpg, "Earth Resistance: {}".format(rpg.player.earth_resist))
        self.earthResist.statDefault(rpg, -70, 350)

        self.windResist = Button(rpg, "Wind Resistance: {}".format(rpg.player.wind_resist))
        self.windResist.statDefault(rpg, -420, 700)

        self.evasion = Button(rpg, "Evasion: {}".format(rpg.player.evasion))
        self.evasion.statDefault(rpg, -350, 700)

        self.accuracyStat = Button(rpg, "Accuracy: {}".format(rpg.player.accuracy))
        self.accuracyStat.statDefault(rpg, -280, 700)
        
        self.critStat = Button(rpg, "Crit Chance: {}".format(rpg.player.crit_chance))
        self.critStat.statDefault(rpg, -210, 700)

        self.critMult = Button(rpg, "Crit Multiplier: {}".format(rpg.player.crit_mult))
        self.critMult.statDefault(rpg, -140, 700)

        self.luckStat = Button(rpg, "Luck: {}".format(rpg.player.luck))
        self.luckStat.statDefault(rpg, -70, 700)
        
    def updateStats(self, rpg):
        self.hpStat.msg = "HP: {}/{}".format(rpg.player.hp, rpg.player.maxhp)
        self.stamStat.msg = "Stamina: {}/{}".format(rpg.player.stamina, rpg.player.stamina_max)   
        self.manaStat.msg = "Mana: {}/{}".format(rpg.player.mana, rpg.player.mana_max)
        self.speedStat.msg = "Speed: {}".format(rpg.player.speed)
        self.physAtckStat.msg = "Physical Attack: {}".format(rpg.player.physical_attack)
        self.magicAtckStat.msg = "Magic Attack: {}".format(rpg.player.magic_attack)
        self.physDefStat.msg = "Physical Defense: {}".format(rpg.player.physical_defense)
        self.magicDefStat.msg = "Magic Defense: {}".format(rpg.player.magic_defense)
        self.fireResist.msg = "Fire Resistance: {}".format(rpg.player.fire_resist)
        self.poisonResist.msg = "Poison Resistance: {}".format(rpg.player.poison_resist)
        self.waterResist.msg = "Water Resistance: {}".format(rpg.player.water_resist)
        self.earthResist.msg = "Earth Resistance: {}".format(rpg.player.earth_resist)
        self.windResist.msg = "Wind Resistance: {}".format(rpg.player.wind_resist)
        self.evasion.msg = "Evasion: {}".format(rpg.player.evasion)
        self.accuracyStat.msg = "Accuracy: {}".format(rpg.player.accuracy)
        self.critStat.msg = "Crit Chance: {}".format(rpg.player.crit_chance)
        self.critMult.msg = "Crit Multiplier: {}".format(rpg.player.crit_mult)
        self.luckStat.msg = "Luck: {}".format(rpg.player.luck)

    def showStats(self, rpg):
        self.updateStats(rpg)
        self.hpStat.draw()
        self.stamStat.draw()
        self.manaStat.draw()
        self.speedStat.draw()
        self.physAtckStat.draw()
        self.magicAtckStat.draw()
        self.physDefStat.draw()
        self.magicDefStat.draw()
        self.fireResist.draw()
        self.poisonResist.draw()
        self.waterResist.draw()
        self.earthResist.draw()
        self.windResist.draw()
        self.evasion.draw()
        self.accuracyStat.draw()
        self.critStat.draw()
        self.critMult.draw()
        self.luckStat.draw()


class borders:
    def __init__(self, rpg):
        #OuterBorder
        self.borderSquare = square(rpg)

        #MapBorder
        self.mapSquare = square(rpg)
        self.mapSquare.height = self.borderSquare.height - 420

        #TextBorder
        self.textSquare = square(rpg)
        self.textSquare.height = self.textSquare.height - 420
        self.textSquare.width = 1050
   
    def draw(self):
        self.borderSquare.draw()
        self.mapSquare.draw()
        self.textSquare.draw()

class swapButton:
    def __init__(self, rpg):
        self.swapButton = image(rpg, 'CREATE Task Folder\Image Assets\GUI_images\Bag.png', "Player Inventory")#pylint: disable = anomalous-backslash-in-string
        self.swapButton.width = (rpg.settings.screen_width - 1600)
        self.swapButton.height = 210
        self.swapButton.top = (rpg.settings.screen_height) - self.swapButton.height
        self.swapButton.left = 1050
        self.swapButton.border = True
        self.swapButton.clickable = True
        self.inventoryShow = False
        self.statsShow = True

    def mouseEvents(self, mous_pos):
        if self.swapButton.rect.collidepoint(mous_pos):
            if self.inventoryShow == True:
                self.inventoryShow = False
            else:
                self.inventoryShow = True
            self.swap()

    def swap(self):
        if self.swapButton.msg == "Player Inventory":
            self.stats()
        elif self.swapButton.msg == "Stat Sheet":
            self.inventory()

    def stats(self):
        self.swapButton.image = pygame.image.load('CREATE Task Folder\Image Assets\GUI_images\Stat Sheet.gif')#pylint: disable = anomalous-backslash-in-string
        self.swapButton.msg = "Stat Sheet"

    def inventory(self):
        self.swapButton.image = pygame.image.load('CREATE Task Folder\Image Assets\GUI_images\Bag.png')#pylint: disable = anomalous-backslash-in-string
        self.swapButton.msg = "Player Inventory"

    def draw(self):
        self.swapButton.draw()

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
                #self.ally1Icon = image(rpg, rpg.player.equipped_allies[0].icon, rpg.player.equipped_allies[0].name)
                #self.ally1Icon.iconDefault(rpg, -210)
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
                #self.ally2Icon = image(rpg, rpg.player.equipped_allies[1].icon, rpg.player.equipped_allies[1].name)
                #self.ally2Icon.iconDefault(rpg, -105)
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
                #self.ally3Icon = image(rpg, rpg.player.equipped_allies[2].icon, rpg.player.equipped_allies[2].name)
                #self.ally3Icon.iconDefault(rpg, 0)
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
    
    def draw(self):
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
        

class profilePic:
    def __init__(self, rpg):
        self.profilePic = image(rpg, 'CREATE Task Folder\Image Assets\Player_Images\Commoner.png', rpg.player.profession + " EXP: {}/{}".format(rpg.player.exp, rpg.player.exp_cap))#pylint: disable = anomalous-backslash-in-string
        self.profilePic.font.set_bold(True)
        self.profilePic.width = (rpg.settings.screen_width - 1600)
        self.profilePic.height = 210
        self.profilePic.top = (rpg.settings.screen_height) - (self.profilePic.height*2)
        self.profilePic.left = 1050
        self.profilePic.border = True
        self.profilePic.textMidBottom = True
    
    def swapImage(self, path):
        self.profilePic.image = pygame.image.load(path)
    
    def draw(self):
        self.profilePic.draw()

class playerConsole:
    def __init__(self, rpg):
        self.newSlot = 0
        self.slot1Taken = 0
        self.slot2Taken = 0
        self.slot3Taken = 0
        self.slot4Taken = 0
        self.slot5Taken = 0
        self.icon5 = image(rpg, "CREATE Task Folder\Image Assets\Weapon_Images\CopperShiv.png", "")
        self.icon5.consoleDefault(rpg, 0)
        self.slot5 = Button(rpg, "")
        self.slot5.consoleTextDefault(rpg, 0)
        self.icon4 = image(rpg, "CREATE Task Folder\Image Assets\Weapon_Images\CopperSword.png", "")
        self.icon4.consoleDefault(rpg, 132)
        self.slot4 = Button(rpg, "")
        self.slot4.consoleTextDefault(rpg, 132)
        self.icon3 = image(rpg, "CREATE Task Folder\Image Assets\Capture (1).png", "")
        self.icon3.consoleDefault(rpg, 264)
        self.slot3 = Button(rpg, "")
        self.slot3.consoleTextDefault(rpg, 264)
        self.icon2 = image(rpg, "CREATE Task Folder\Image Assets\GUI_images\ArmorTag.png", "")
        self.icon2.consoleDefault(rpg, 396)
        self.slot2 = Button(rpg, "")
        self.slot2.consoleTextDefault(rpg, 396)
        self.icon1 = image(rpg, "CREATE Task Folder\Image Assets\GUI_images\BuffTag.png", "")
        self.icon1.consoleDefault(rpg, 528)
        self.slot1 = Button(rpg, "")
        self.slot1.consoleTextDefault(rpg, 528)

    def drawConsole(self):
        self.slot1.draw()
        self.icon1.draw()
        self.slot2.draw()
        self.icon2.draw()
        self.slot3.draw()
        self.icon3.draw()
        self.slot4.draw()
        self.icon4.draw()
        self.slot5.draw()
        self.icon5.draw()
       
    def showNextText(self, nextText, nextTextPart2, nextIcon):
        self.slot5.msg = self.slot4.msg
        self.slot5.msg2 = self.slot4.msg2
        self.icon5.image = self.icon4.image
        self.slot4.msg = self.slot3.msg
        self.slot4.msg2 = self.slot3.msg2
        self.icon4.image = self.icon3.image
        self.slot3.msg = self.slot2.msg
        self.slot3.msg2 = self.slot2.msg2
        self.icon3.image = self.icon2.image
        self.slot2.msg = self.slot1.msg
        self.slot2.msg2 = self.slot1.msg2
        self.icon2.image = self.icon1.image
        self.slot1.msg = nextText
        self.slot1.msg2 = nextTextPart2
        self.icon1.image = nextIcon

    def resetConsole(self):
        self.slot5.msg = ""
        self.slot4.msg = ""
        self.slot3.msg = ""
        self.slot2.msg = ""
        self.slot1.msg = ""
        self.slot5.msg2 = ""
        self.slot4.msg2 = ""
        self.slot3.msg2 = ""
        self.slot2.msg2 = ""
        self.slot1.msg2 = ""

