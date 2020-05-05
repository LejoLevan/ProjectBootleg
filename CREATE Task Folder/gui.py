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
        

    def showStats(self):
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

class profilePic:
    def __init__(self, rpg):
        self.profilePic = image(rpg, 'CREATE Task Folder\Image Assets\Player_Images\Commoner.png', rpg.player.profession)#pylint: disable = anomalous-backslash-in-string
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

class Inventory:
    def __init__(self, rpg):
        self.upArrow = image(rpg, 'CREATE Task Folder\Image Assets\GUI_images\Arrow.png', "")#pylint: disable = anomalous-backslash-in-string
        self.upArrow.width = 50
        self.upArrow.height = 210
        self.upArrow.top = (rpg.settings.screen_height) - (self.upArrow.height*2)
        self.upArrow.left = 1000
        self.upArrow.clickable = True
        self.upArrow.border = True

        self.downArrow = image(rpg, 'CREATE Task Folder\Image Assets\GUI_images\downArrow.png', "")#pylint: disable = anomalous-backslash-in-string
        self.downArrow.width = 50
        self.downArrow.height = 210
        self.downArrow.top = (rpg.settings.screen_height) - self.downArrow.height
        self.downArrow.left = 1000
        self.downArrow.border = True
        self.downArrow.clickable = True

        self.weapon_inventory = rpg.player.weapon_inventory
        self.armor_inventory = rpg.player.armor_inventory
        self.buff_inventory = rpg.player.buff_inventory
        self.misc_inventory = rpg.player.misc_inventory
        self.quest_inventory = rpg.player.quest_inventory

        self.set = 0
        self.list = self.weapon_inventory
        self.msgList = []
        
        self.box1 = Button(rpg, self.getMsg(self.set + 1))
        self.box1.inventoryDefault(rpg, -360, 0)
        self.box2 = Button(rpg, self.getMsg(self.set + 2))
        self.box2.inventoryDefault(rpg, -300, 0)
        self.box3 = Button(rpg, self.getMsg(self.set + 3))
        self.box3.inventoryDefault(rpg, -240, 0)
        self.box4 = Button(rpg, self.getMsg(self.set + 4))
        self.box4.inventoryDefault(rpg, -180, 0)
        self.box5 = Button(rpg, self.getMsg(self.set + 5))
        self.box5.inventoryDefault(rpg, -120, 0)
        self.box6 = Button(rpg, self.getMsg(self.set + 6))
        self.box6.inventoryDefault(rpg, -60, 0)

        self.box7 = Button(rpg, self.getMsg(self.set + 7))
        self.box7.inventoryDefault(rpg, -360, 333.33)
        self.box8 = Button(rpg, self.getMsg(self.set + 8))
        self.box8.inventoryDefault(rpg, -300, 333.33)
        self.box9 = Button(rpg, self.getMsg(self.set + 9))
        self.box9.inventoryDefault(rpg, -240, 333.33)
        self.box10 = Button(rpg, self.getMsg(self.set + 10))
        self.box10.inventoryDefault(rpg, -180, 333.33)
        self.box11 = Button(rpg, self.getMsg(self.set + 11))
        self.box11.inventoryDefault(rpg, -120, 333.33)
        self.box12 = Button(rpg, self.getMsg(self.set + 12))
        self.box12.inventoryDefault(rpg, -60, 333.33)

        self.box13 = Button(rpg, self.getMsg(self.set + 13))
        self.box13.inventoryDefault(rpg, -360, 666.67)
        self.box14 = Button(rpg, self.getMsg(self.set + 14))
        self.box14.inventoryDefault(rpg, -300, 666.67)
        self.box15 = Button(rpg, self.getMsg(self.set + 15))
        self.box15.inventoryDefault(rpg, -240, 666.67)
        self.box16 = Button(rpg, self.getMsg(self.set + 16))
        self.box16.inventoryDefault(rpg, -180, 666.67)
        self.box17 = Button(rpg, self.getMsg(self.set + 17))
        self.box17.inventoryDefault(rpg, -120, 666.67)
        self.box18 = Button(rpg, self.getMsg(self.set + 18))
        self.box18.inventoryDefault(rpg, -60, 666.67)

        self.weaponTag = image(rpg, 'CREATE Task Folder\Image Assets\GUI_images\WeaponTag.png', "Weapon Inventory")#pylint: disable = anomalous-backslash-in-string
        self.weaponTag.tagDefault(rpg, 0)
        self.armorTag = image(rpg, 'CREATE Task Folder\Image Assets\GUI_images\ArmorTag.png', "Armor Inventory")#pylint: disable = anomalous-backslash-in-string
        self.armorTag.tagDefault(rpg, 180)
        self.buffTag = image(rpg, 'CREATE Task Folder\Image Assets\GUI_images\BuffTag.png', "Buff Inventory")#pylint: disable = anomalous-backslash-in-string
        self.buffTag.tagDefault(rpg, 360)
        self.miscTag = image(rpg, 'CREATE Task Folder\Image Assets\GUI_images\MiscTag.png', "Misc Inventory")#pylint: disable = anomalous-backslash-in-string
        self.miscTag.tagDefault(rpg, 540)
        self.questTag = image(rpg, 'CREATE Task Folder\Image Assets\GUI_images\QuestTag.png', "Quest Inventory")#pylint: disable = anomalous-backslash-in-string
        self.questTag.tagDefault(rpg, 720)

        self.gold = image(rpg, 'CREATE Task Folder\Image Assets\GUI_images\GoldTag.png', "Gold: {}".format(rpg.player.gold))#pylint: disable = anomalous-backslash-in-string
        self.gold.tagDefault(rpg, 899.99)
        self.gold.width = 100
        self.gold.clickable = False

    def getMsg(self, number):
        stack = 0
        msg = ""
        msgThere = False
        try:
            while msgThere == False:
                msg = self.list[number - 1]
                if msg not in self.msgList:
                    stack = stack + self.list.count(msg)
                    self.msgList.append(msg)
                    msgThere = True
                    return ("{} x{}".format(msg, stack))
                else:
                    number = number + 1
        except Exception:
            return("")
    
    def mouseEvents(self, mous_pos):
        if self.downArrow.rect.collidepoint(mous_pos):
            self.set = self.set + 18
            if self.set > 90:
                self.set = 0
        if self.upArrow.rect.collidepoint(mous_pos):
            self.set = self.set - 18
            if self.set < 0:
                self.set = 0
        if self.weaponTag.rect.collidepoint(mous_pos):
            self.list = self.weapon_inventory
            self.set = 0
        if self.armorTag.rect.collidepoint(mous_pos):
            self.list = self.armor_inventory
            self.set = 0
        if self.buffTag.rect.collidepoint(mous_pos):
            self.list = self.buff_inventory
            self.set = 0
        if self.miscTag.rect.collidepoint(mous_pos):
            self.list = self.misc_inventory
            self.set = 0
        if self.questTag.rect.collidepoint(mous_pos):
            self.list = self.quest_inventory
            self.set = 0

    def update(self, rpg):
        self.msgList = []
        self.box1.msg = self.getMsg(self.set + 1)
        self.box2.msg = self.getMsg(self.set + 2)
        self.box3.msg = self.getMsg(self.set + 3)
        self.box4.msg = self.getMsg(self.set + 4)
        self.box5.msg = self.getMsg(self.set + 5)
        self.box6.msg = self.getMsg(self.set + 6)
        self.box7.msg = self.getMsg(self.set + 7)
        self.box8.msg = self.getMsg(self.set + 8)
        self.box9.msg = self.getMsg(self.set + 9)
        self.box10.msg = self.getMsg(self.set + 10)
        self.box11.msg = self.getMsg(self.set + 11)
        self.box12.msg = self.getMsg(self.set + 12)
        self.box13.msg = self.getMsg(self.set + 13)
        self.box14.msg = self.getMsg(self.set + 14)
        self.box15.msg = self.getMsg(self.set + 15)
        self.box16.msg = self.getMsg(self.set + 16)
        self.box17.msg = self.getMsg(self.set + 17)
        self.box18.msg = self.getMsg(self.set + 18)

        self.weapon_inventory = rpg.player.weapon_inventory
        self.armor_inventory = rpg.player.armor_inventory
        self.buff_inventory = rpg.player.buff_inventory
        self.misc_inventory = rpg.player.misc_inventory
        self.quest_inventory = rpg.player.quest_inventory

    def draw(self, rpg):
        self.update(rpg)

        self.upArrow.draw()
        self.downArrow.draw()

        self.box1.draw()
        self.box2.draw()
        self.box3.draw()
        self.box4.draw()
        self.box5.draw()
        self.box6.draw()
        self.box7.draw()
        self.box8.draw()
        self.box9.draw()
        self.box10.draw()
        self.box11.draw()
        self.box12.draw()
        self.box13.draw()
        self.box14.draw()
        self.box15.draw()
        self.box16.draw()
        self.box17.draw()
        self.box18.draw()

        self.weaponTag.draw()
        self.armorTag.draw()
        self.buffTag.draw()
        self.miscTag.draw()
        self.questTag.draw()
        self.gold.draw()
