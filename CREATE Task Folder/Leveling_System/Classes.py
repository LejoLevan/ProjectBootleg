class Classes:
    def __init__(self, player):
        self.profession = player.profession
        self.level = player.level

    def Squire(self):
        if (self.profession == "Squire" and self.level == 3):
            self.profession = "Knight"
        elif (self.profession == "Squire" and self.level == 10):
            self.profession = "Templar"
        elif (self.profession == "Squire" and self.level == 20):
            self.profession = "Holy Paladin"

    def Thief(self):
        if (self.profession == "Thief" and self.level == 3):
            self.profession = "Scoundrel"
        elif (self.profession == "Thief" and self.level == 10):
            self.profession = "Rogue"
        elif (self.profession == "Thief" and self.level == 20):
            self.profession = "Assassin"

    def Apprentice(self):
        if (self.profession == "Apprentice" and self.level == 3):
            self.profession = "Warlock"
        elif (self.profession == "Apprentice" and self.level == 10):
            self.profession = "Wizard"
        elif (self.profession == "Apprentice" and self.level == 20):
            self.profession = "Head Mage"
        
    def Commoner(self):
        if (self.profession == "Commoner" and self.level == 3):
            self.profession = "Soldier"
        elif (self.profession == "Commoner" and self.level == 10):
            self.profession = "Noble"
        elif (self.profession == "Commoner" and self.level == 20):
            self.profession = "Great Lord"

    def Warrior(self):
        if (self.profession == "Warrior" and self.level == 0):
            self.profession = "Warrior"
        elif (self.profession == "Warrior" and self.level == 3):
            self.profession = "Berserker"
        elif (self.profession == "Warrior" and self.level == 10):
            self.profession = "Gladiator"
        elif (self.profession == "Warrior" and self.level == 20):
            self.profession = "Slayer"

    def Archer(self):
        if (self.profession == "Archer" and self.level == 0):
           self.profession = "Archer"
        elif (self.profession == "Archer" and self.level == 3):
            self.profession = "Hunter"
        elif (self.profession == "Archer" and self.level == 10):
            self.profession = "Marksman"
        elif (self.profession == "Archer" and self.level == 20):
            self.profession = "Ranger"
    
    def updateClass(self):
        Classes.Archer(self)
        Classes.Warrior(self)
        Classes.Commoner(self)
        Classes.Apprentice(self)
        Classes.Thief(self)
        Classes.Squire(self)
        return (self.profession)
