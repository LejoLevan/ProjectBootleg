from GUI_Components.button import Button
from GUI_Components.square import square
from GUI_Components.image import image

class mainMenu():
    def __init__(self, rpg):
        #LoadButton Settings
        self.loadButton = Button(rpg, "Load")
        self.loadButton.startDefault(rpg, 75, 0)
        
        #OuterBorder
        self.borderSquare = square(rpg)
        self.borderSquare.width = rpg.settings.screen_width
        self.borderSquare.height = rpg.settings.screen_height
        self.borderSquare.top = 0
        self.borderSquare.left = 0
        self.borderSquare.color = (255, 255, 255)
        self.borderSquare.border = 1
        
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

        self.borderSquare.draw()

class choiceButtons():
    def __init__(self, rpg):
        self.choice1 = Button(rpg, "")
        self.choice1.choiceDefault(rpg, -375, 0)
        
        self.choice2 = Button(rpg, "")
        self.choice2.choiceDefault(rpg, -300, 0)
        
        self.choice3 = Button(rpg, "")
        self.choice3.choiceDefault(rpg, -225, 0)
        
        self.choice4 = Button(rpg, "")
        self.choice4.choiceDefault(rpg, -150, 0)
        
        self.choice5 = Button(rpg, "")
        self.choice5.choiceDefault(rpg, -75, 0)
        
        self.choice6 = Button(rpg, "")
        self.choice6.choiceDefault(rpg, 0, 0)

    def draw(self):
        self.choice1.draw()

        self.choice2.draw()

        self.choice3.draw()

        self.choice4.draw()

        self.choice5.draw()

        self.choice6.draw()
        
    def editChoices(self,choice1Text,choice2Text,choice3Text,choice4Text,choice5Text,choice6Text):
        self.choice1.msg = choice1Text
        self.choice2.msg = choice2Text
        self.choice3.msg = choice3Text
        self.choice4.msg = choice4Text
        self.choice5.msg = choice5Text
        self.choice6.msg = choice6Text

class statSheet():
    def __init__(self, rpg):
        self.hpStat = Button(rpg, "")
        self.hpStat.statDefault(rpg, -375, 0, "HP: {}/{}".format(rpg.player.hp, rpg.player.maxhp))
        self.stamStat = Button(rpg, "")
        self.stamStat.statDefault(rpg, -300, 0, "Stamina: {}/{}".format(rpg.player.stamina, rpg.player.stamina_max))
        self.manaStat = Button(rpg, "")
        self.manaStat.statDefault(rpg, -225, 0, "Mana: {}/{}".format(rpg.player.mana, rpg.player.mana_max))
        self.speedStat = Button(rpg, "")
        self.speedStat.statDefault(rpg, -150, 0, "Speed: {}".format(rpg.player.speed))
        self.physAtckStat = Button(rpg, "")
        self.physAtckStat.statDefault(rpg, -75, 0, "Physical Attack: {}".format(rpg.player.physical_attack))
        self.magicAtckStat = Button(rpg, "")
        self.magicAtckStat.statDefault(rpg, 0, 0, "Magic Attack: {}".format(rpg.player.magic_attack))
        self.physDefStat = Button(rpg, "")
        self.physDefStat.statDefault(rpg, -375, -200, "Physical Defense: {}".format(rpg.player.physical_defense))
        self.magicDefStat = Button(rpg, "")
        self.magicDefStat.statDefault(rpg, -300, -200, "Magic Defense: {}".format(rpg.player.magic_defense))
        self.fireResist = Button(rpg, "")
        self.fireResist.statDefault(rpg, -225, -200, "Fire Resistance: {}".format(rpg.player.fire_resist))
        self.poisonResist = Button(rpg, "")
        self.poisonResist.statDefault(rpg, -150, -200, "Poison Resistance: {}".format(rpg.player.poison_resist))
        self.accuracyStat = Button(rpg, "")
        self.accuracyStat.statDefault(rpg, -75, -200, "Accuracy: {}".format(rpg.player.accuracy))
        self.critStat = Button(rpg, "")
        self.critStat.statDefault(rpg, 0, -200, "Crit Chance: {}".format(rpg.player.crit_chance))
        self.critMult = Button(rpg, "")
        self.critMult.statDefault(rpg, -375, -400, "Crit Multiplier: {}".format(rpg.player.crit_mult))
        self.luckStat = Button(rpg, "")
        self.luckStat.statDefault(rpg, -300, -400, "Luck: {}".format(rpg.player.luck))
        

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
        self.accuracyStat.draw()
        self.critStat.draw()
        self.critMult.draw()
        self.luckStat.draw()