import pygame

from GUI_Components.button import Button
from GUI_Components.square import square
from GUI_Components.image import image

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

        self.notificationImage = image(rpg, 'CREATE Task Folder\Image Assets\Weapon_Images\Copper Sword Info.png', "")
        self.notificationImage.width = 800
        self.notificationImage.height = 196
        self.notificationImage.top = (rpg.settings.screen_height) - 331
        self.notificationImage.left = 99.995
        self.notificationImage.border = True

        self.infoBox = square(rpg)
        self.infoBox.width = 266.67
        self.infoBox.height = 196
        self.infoBox.top = (rpg.settings.screen_height) - 331
        self.infoBox.left = 99.995

        self.okButton = Button(rpg, "Ok")
        self.okButton.width = 266.67
        self.okButton.height = 40
        self.okButton.top = (rpg.settings.screen_height) - 135
        self.okButton.left = 99.995

        self.equipButton = Button(rpg, "Equip")
        self.equipButton.width = 266.67
        self.equipButton.height = 40
        self.equipButton.top = (rpg.settings.screen_height) - 135
        self.equipButton.left = 366.66

        self.deleteButton = Button(rpg, "Delete")
        self.deleteButton.width = 266.67
        self.deleteButton.height = 40
        self.deleteButton.top = (rpg.settings.screen_height) - 135
        self.deleteButton.left = 633.33

        self.infoShow = False
        self.equipItem = None

        self.blackScreen = Button (rpg, "")
        self.blackScreen.width = 999.99
        self.blackScreen.height = 420
        self.blackScreen.top = rpg.settings.screen_height - 420
        self.blackScreen.left = 0
        self.blackScreen.clickable = False

        self.weapons = rpg.player.weapons
        self.weapon_inventory = rpg.player.weapon_inventory
        self.armors = rpg.player.armors
        self.armor_inventory = rpg.player.armor_inventory
        self.buffs = rpg.player.buffs
        self.buff_inventory = rpg.player.buff_inventory
        self.miscs = rpg.player.miscs
        self.misc_inventory = rpg.player.misc_inventory
        self.quest_items = rpg.player.quest_items
        self.quest_inventory = rpg.player.quest_inventory

        self.set = 0
        self.list = self.weapon_inventory
        self.inventory = "Weapon Inventory"
        self.namelist = self.weapons
        self.msgList = []
        self.iconList = []
        self.infoList = []
        
        self.icon1 = image(rpg, self.get(self.set +1, "Icon"), "")
        self.icon1.inventoryDefault(rpg, -360, 0)
        self.box1 = Button(rpg, self.get(self.set + 1, "Msg"))
        self.box1.inventoryDefault(rpg, -360, 0)

        self.icon2 = image(rpg, self.get(self.set + 2, "Icon"), "")
        self.icon2.inventoryDefault(rpg, -300, 0)
        self.box2 = Button(rpg, self.get(self.set + 2, "Msg"))
        self.box2.inventoryDefault(rpg, -300, 0)

        self.icon3 = image(rpg, self.get(self.set + 3, "Icon"), "")
        self.icon3.inventoryDefault(rpg, -240, 0)
        self.box3 = Button(rpg, self.get(self.set + 3, "Msg"))
        self.box3.inventoryDefault(rpg, -240, 0)

        self.icon4 = image(rpg, self.get(self.set + 4, "Icon"), "")
        self.icon4.inventoryDefault(rpg, -180, 0)
        self.box4 = Button(rpg, self.get(self.set + 4, "Msg"))
        self.box4.inventoryDefault(rpg, -180, 0)

        self.icon5 = image(rpg, self.get(self.set + 5, "Icon"), "")
        self.icon5.inventoryDefault(rpg, -120, 0)
        self.box5 = Button(rpg, self.get(self.set + 5, "Msg"))
        self.box5.inventoryDefault(rpg, -120, 0)

        self.icon6 = image(rpg, self.get(self.set + 6, "Icon"), "")
        self.icon6.inventoryDefault(rpg, -60, 0)
        self.box6 = Button(rpg, self.get(self.set + 6, "Msg"))
        self.box6.inventoryDefault(rpg, -60, 0)

        self.icon7 = image(rpg, self.get(self.set + 7, "Icon"), "")
        self.icon7.inventoryDefault(rpg, -360, 333.33)
        self.box7 = Button(rpg, self.get(self.set + 7, "Msg"))
        self.box7.inventoryDefault(rpg, -360, 333.33)

        self.icon8 = image(rpg, self.get(self.set + 8, "Icon"), "")
        self.icon8.inventoryDefault(rpg, -300, 333.33)
        self.box8 = Button(rpg, self.get(self.set + 8, "Msg"))
        self.box8.inventoryDefault(rpg, -300, 333.33)

        self.icon9 = image(rpg, self.get(self.set + 9, "Icon"), "")
        self.icon9.inventoryDefault(rpg, -240, 333.33)
        self.box9 = Button(rpg, self.get(self.set + 9, "Msg"))
        self.box9.inventoryDefault(rpg, -240, 333.33)
        
        self.icon10 = image(rpg, self.get(self.set + 10, "Icon"), "")
        self.icon10.inventoryDefault(rpg, -180, 333.33)
        self.box10 = Button(rpg, self.get(self.set + 10, "Msg"))
        self.box10.inventoryDefault(rpg, -180, 333.33)

        self.icon11 = image(rpg, self.get(self.set + 11, "Icon"), "")
        self.icon11.inventoryDefault(rpg, -120, 333.33)
        self.box11 = Button(rpg, self.get(self.set + 11, "Msg"))
        self.box11.inventoryDefault(rpg, -120, 333.33)

        self.icon12 = image(rpg, self.get(self.set + 12, "Icon"), "")
        self.icon12.inventoryDefault(rpg, -60, 333.33)
        self.box12 = Button(rpg, self.get(self.set + 12, "Msg"))
        self.box12.inventoryDefault(rpg, -60, 333.33)

        self.icon13 = image(rpg, self.get(self.set + 13, "Icon"), "")
        self.icon13.inventoryDefault(rpg, -360, 666.67)
        self.box13 = Button(rpg, self.get(self.set + 13, "Msg"))
        self.box13.inventoryDefault(rpg, -360, 666.67)

        self.icon14 = image(rpg, self.get(self.set + 14, "Icon"), "")
        self.icon14.inventoryDefault(rpg, -300, 666.67)
        self.box14 = Button(rpg, self.get(self.set + 14, "Msg"))
        self.box14.inventoryDefault(rpg, -300, 666.67)

        self.icon15 = image(rpg, self.get(self.set + 15, "Icon"), "")
        self.icon15.inventoryDefault(rpg, -240, 666.67)
        self.box15 = Button(rpg, self.get(self.set + 15, "Msg"))
        self.box15.inventoryDefault(rpg, -240, 666.67)

        self.icon16 = image(rpg, self.get(self.set + 16, "Icon"), "")
        self.icon16.inventoryDefault(rpg, -180, 666.67)
        self.box16 = Button(rpg, self.get(self.set + 16, "Msg"))
        self.box16.inventoryDefault(rpg, -180, 666.67)

        self.icon17 = image(rpg, self.get(self.set + 17, "Icon"), "")
        self.icon17.inventoryDefault(rpg, -120, 666.67)
        self.box17 = Button(rpg, self.get(self.set + 17, "Msg"))
        self.box17.inventoryDefault(rpg, -120, 666.67)

        self.icon18 = image(rpg, self.get(self.set + 18, "Icon"), "")
        self.icon18.inventoryDefault(rpg, -60, 666.67)
        self.box18 = Button(rpg, self.get(self.set + 18, "Msg"))
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

    def get(self, number, what):
        if what == "Msg":
            stack = 0
            msg = ""
            msgThere = False
            try:
                while msgThere == False:
                    msg = self.namelist[number - 1]
                    if msg not in self.msgList:
                        stack = stack + self.namelist.count(msg)
                        self.msgList.append(msg)
                        msgThere = True
                        return ("{} x{}".format(msg, stack))
                    else:
                        number = number + 1
            except Exception:
                return("")
        elif what == "Icon":
            icon = ""
            iconThere = False
            try:
                while iconThere == False:
                    icon = self.list[number - 1].icon
                    if icon not in self.iconList:
                        self.iconList.append(icon)
                        iconThere = True
                        return(icon)
                    else:
                        number = number + 1
            except Exception:
                return('CREATE Task Folder\Image Assets\Transparent.png')
        elif what == "Info":
            info = ""
            infoThere = False
            try:
                while infoThere == False:
                    info = self.list[number - 1].info
                    if info not in self.infoList:
                        self.infoList.append(info)
                        infoThere = True
                        self.equipItem = self.list[number - 1]
                        return(info)
                    else:
                        number = number + 1
            except Exception:
                return('CREATE Task Folder\Image Assets\Transparent.png')

    def mouseEvents(self, rpg, mous_pos):
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
            self.inventory = "Weapon Inventory"
            self.namelist = self.weapons
            self.set = 0
        if self.armorTag.rect.collidepoint(mous_pos):
            self.list = self.armor_inventory
            self.inventory = "Armor Inventory"
            self.namelist = self.armors
            self.set = 0
        if self.buffTag.rect.collidepoint(mous_pos):
            self.list = self.buff_inventory
            self.inventory = "Buff Inventory"
            self.namelist = self.buffs
            self.set = 0
        if self.miscTag.rect.collidepoint(mous_pos):
            self.list = self.misc_inventory
            self.inventory = "Misc Inventory"
            self.namelist = self.miscs
            self.set = 0
        if self.questTag.rect.collidepoint(mous_pos):
            self.list = self.quest_inventory
            self.inventory = "Quest Inventory"
            self.namelist = self.quest_items
            self.set = 0
        if self.box1.rect.collidepoint(mous_pos):
            self.info(self.set + 1)
        if self.okButton.rect.collidepoint(mous_pos) and self.infoShow == True:
            self.infoShow = False
        if self.equipButton.rect.collidepoint(mous_pos) and self.infoShow == True:
            try:
                if self.equipButton.msg == "Equip":
                    rpg.player.weapon_equipped = self.equipItem
                elif self.equipButton.msg == "Use":
                    rpg.player.useBuff(self.equipItem)
            except Exception:
                pass
            self.infoShow = False
        if self.deleteButton.rect.collidepoint(mous_pos) and self.infoShow  == True:
            try:
                rpg.player.deleteInventory(self.inventory, self.equipItem)
            except Exception:
                pass
            self.infoShow = False
        self.update(rpg)

    def info(self, number):
        self.infoShow = True
        if self.list == self.weapon_inventory or self.list == self.armor_inventory:
            self.notificationImage.image = pygame.image.load(self.get(number, "Info"))
            self.equipButton.msg = "Equip"
        elif self.list == self.buff_inventory:
            self.equipButton.msg = "Use"
            self.notificationImage.image = pygame.image.load(self.get(number, "Info"))
        elif self.list == self.misc_inventory or self.list == self.quest_inventory:
            self.equipButton.msg = ""
            self.notificationImage.image = pygame.image.load(self.get(number, "Info"))

    def update(self, rpg):
        self.msgList = []
        self.iconList = []
        self.infoList = []
        self.gold.msg = ("Gold: {}".format(rpg.player.gold))
        self.box1.msg = self.get(self.set + 1, "Msg")
        self.icon1.image = pygame.image.load(self.get(self.set + 1, "Icon")).convert_alpha()
        self.box2.msg = self.get(self.set + 2, "Msg")
        self.icon2.image = pygame.image.load(self.get(self.set + 2, "Icon")).convert_alpha()
        self.box3.msg = self.get(self.set + 3, "Msg")
        self.icon3.image = pygame.image.load(self.get(self.set + 3, "Icon")).convert_alpha()
        self.box4.msg = self.get(self.set + 4, "Msg")
        self.icon4.image = pygame.image.load(self.get(self.set + 4, "Icon")).convert_alpha()
        self.box5.msg = self.get(self.set + 5, "Msg")
        self.icon5.image = pygame.image.load(self.get(self.set + 5, "Icon")).convert_alpha()
        self.box6.msg = self.get(self.set + 6, "Msg")
        self.icon6.image = pygame.image.load(self.get(self.set + 6, "Icon")).convert_alpha()
        self.box7.msg = self.get(self.set + 7, "Msg")
        self.icon7.image = pygame.image.load(self.get(self.set + 7, "Icon")).convert_alpha()
        self.box8.msg = self.get(self.set + 8, "Msg")
        self.icon8.image = pygame.image.load(self.get(self.set + 8, "Icon")).convert_alpha()
        self.box9.msg = self.get(self.set + 9, "Msg")
        self.icon9.image = pygame.image.load(self.get(self.set + 9, "Icon")).convert_alpha()
        self.box10.msg = self.get(self.set + 10, "Msg")
        self.icon10.image = pygame.image.load(self.get(self.set + 10, "Icon")).convert_alpha()
        self.box11.msg = self.get(self.set + 11, "Msg")
        self.icon11.image = pygame.image.load(self.get(self.set + 11, "Icon")).convert_alpha()
        self.box12.msg = self.get(self.set + 12, "Msg")
        self.icon12.image = pygame.image.load(self.get(self.set + 12, "Icon")).convert_alpha()
        self.box13.msg = self.get(self.set + 13, "Msg")
        self.icon13.image = pygame.image.load(self.get(self.set + 13, "Icon")).convert_alpha()
        self.box14.msg = self.get(self.set + 14, "Msg")
        self.icon14.image = pygame.image.load(self.get(self.set + 14, "Icon")).convert_alpha()
        self.box15.msg = self.get(self.set + 15, "Msg")
        self.icon15.image = pygame.image.load(self.get(self.set + 15, "Icon")).convert_alpha()
        self.box16.msg = self.get(self.set + 16, "Msg")
        self.icon16.image = pygame.image.load(self.get(self.set + 16, "Icon")).convert_alpha()
        self.box17.msg = self.get(self.set + 17, "Msg")
        self.icon17.image = pygame.image.load(self.get(self.set + 17, "Icon")).convert_alpha()
        self.box18.msg = self.get(self.set + 18, "Msg")
        self.icon18.image = pygame.image.load(self.get(self.set + 18, "Icon")).convert_alpha()

        self.weapons = rpg.player.weapons
        self.weapon_inventory = rpg.player.weapon_inventory
        self.armors = rpg.player.armors
        self.armor_inventory = rpg.player.armor_inventory
        self.buffs = rpg.player.buffs
        self.buff_inventory = rpg.player.buff_inventory
        self.miscs = rpg.player.miscs
        self.misc_inventory = rpg.player.misc_inventory
        self.quest_items = rpg.player.quest_items
        self.quest_inventory = rpg.player.quest_inventory

    def draw(self, rpg):
        self.upArrow.draw()
        self.downArrow.draw()
        
        self.box1.draw()
        self.icon1.draw()
        self.box2.draw()
        self.icon2.draw()
        self.box3.draw()
        self.icon3.draw()
        self.box4.draw()
        self.icon4.draw()
        self.box5.draw()
        self.icon5.draw()
        self.box6.draw()
        self.icon6.draw()
        self.box7.draw()
        self.icon7.draw()
        self.box8.draw()
        self.icon8.draw()
        self.box9.draw()
        self.icon9.draw()
        self.box10.draw()
        self.icon10.draw()
        self.box11.draw()
        self.icon11.draw()
        self.box12.draw()
        self.icon12.draw()
        self.box13.draw()
        self.icon13.draw()
        self.box14.draw()
        self.icon14.draw()
        self.box15.draw()
        self.icon15.draw()
        self.box16.draw()
        self.icon16.draw()
        self.box17.draw()
        self.icon17.draw()
        self.box18.draw()
        self.icon18.draw()

        self.weaponTag.draw()
        self.armorTag.draw()
        self.buffTag.draw()
        self.miscTag.draw()
        self.questTag.draw()
        self.gold.draw()

        if self.infoShow == True:
            self.blackScreen.draw()
            self.okButton.draw()
            self.deleteButton.draw()
            self.equipButton.draw()
            self.notificationImage.draw()
            self.infoBox.draw()
