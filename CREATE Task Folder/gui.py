from GUI_Components.button import Button
from GUI_Components.square import square
from GUI_Components.image import image

class mainMenu():
    def __init__(self, rpg):
        #LoadButton Settings
        self.loadButton = Button(rpg, "Load")
        self.loadButton.startDefault(75, 0)
          
        #New game button
        self.newGameButton = Button(rpg, "New Game")
        self.newGameButton.startDefault(0, 0)
        
        #Quit Button
        self.quitButton = Button(rpg, "Quit")
        self.quitButton.startDefault(150, 0)

        #Project Logo
        self.logo = image(rpg, 'CREATE Task Folder\Image Assets\GUI_images\ProjectLogo.png', "")#pylint: disable = anomalous-backslash-in-string
        self.logo.top = 540 - (self.logo.height/2) - 200
        self.logo.left = 960 - (self.logo.width/2)

    def draw(self):
        self.loadButton.draw()

        self.newGameButton.draw()

        self.quitButton.draw()

        self.logo.draw()

class choiceButtons():
    def __init__(self, rpg):
        self.choice1 = Button(rpg, "")
        self.choice1.choiceDefault(0)
        
        self.choice2 = Button(rpg, "")
        self.choice2.choiceDefault(-70)
        
        self.choice3 = Button(rpg, "")
        self.choice3.choiceDefault(-140)
        
        self.choice4 = Button(rpg, "")
        self.choice4.choiceDefault(-210)
        
        self.choice5 = Button(rpg, "")
        self.choice5.choiceDefault(-280)
        
        self.choice6 = Button(rpg, "")
        self.choice6.choiceDefault(-350)

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
        self.hpStat.statDefault(-420, 0)

        self.stamStat = Button(rpg, "Stamina: {}/{}".format(rpg.player.stamina, rpg.player.stamina_max))
        self.stamStat.statDefault(-350, 0)

        self.manaStat = Button(rpg, "Mana: {}/{}".format(rpg.player.mana, rpg.player.mana_max))
        self.manaStat.statDefault(-280, 0)

        self.speedStat = Button(rpg, "Speed: {}".format(rpg.player.speed))
        self.speedStat.statDefault(-210, 0)

        self.physAtckStat = Button(rpg, "Physical Attack: {}".format(rpg.player.physical_attack))
        self.physAtckStat.statDefault(-140, 0)

        self.magicAtckStat = Button(rpg,  "Magic Attack: {}".format(rpg.player.magic_attack))
        self.magicAtckStat.statDefault(-70, 0)
        
        self.physDefStat = Button(rpg, "Physical Defense: {}".format(rpg.player.physical_defense))
        self.physDefStat.statDefault(-420, 350)

        self.magicDefStat = Button(rpg, "Magic Defense: {}".format(rpg.player.magic_defense))
        self.magicDefStat.statDefault(-350, 350)

        self.fireResist = Button(rpg, "Fire Resistance: {}".format(rpg.player.fire_resist))
        self.fireResist.statDefault(-280, 350)

        self.poisonResist = Button(rpg, "Poison Resistance: {}".format(rpg.player.poison_resist))
        self.poisonResist.statDefault(-210, 350)

        self.waterResist = Button(rpg, "Water Resistance: {}".format(rpg.player.water_resist))
        self.waterResist.statDefault(-140, 350)

        self.earthResist = Button(rpg, "Earth Resistance: {}".format(rpg.player.earth_resist))
        self.earthResist.statDefault(-70, 350)

        self.windResist = Button(rpg, "Wind Resistance: {}".format(rpg.player.wind_resist))
        self.windResist.statDefault(-420, 700)

        self.evasion = Button(rpg, "Evasion: {}".format(rpg.player.evasion))
        self.evasion.statDefault(-350, 700)

        self.accuracyStat = Button(rpg, "Accuracy: {}".format(rpg.player.accuracy))
        self.accuracyStat.statDefault(-280, 700)
        
        self.critStat = Button(rpg, "Crit Chance: {}".format(rpg.player.crit_chance))
        self.critStat.statDefault(-210, 700)

        self.critMult = Button(rpg, "Crit Multiplier: {}".format(rpg.player.crit_mult))
        self.critMult.statDefault(-140, 700)

        self.luckStat = Button(rpg, "Luck: {}".format(rpg.player.luck))
        self.luckStat.statDefault(-70, 700)
        

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
        self.mapSquare.height = self.mapSquare.height - 420

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
        self.bagButton = image(rpg, 'CREATE Task Folder\Image Assets\GUI_images\Bag.png', "Player Inventory")
        self.bagButton.width = 320
        self.bagButton.height = 210
        self.bagButton.top = 1080 - self.bagButton.height
        self.bagButton.left = 1050
        self.bagButton.border = True
        self.bagButton.clickable = True

    def draw(self):
        self.bagButton.draw()