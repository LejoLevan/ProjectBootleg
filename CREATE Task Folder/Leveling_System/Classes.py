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
        if (self.profession == "Thief" and self.level == 10):
            self.profession = "Rogue"
        if (self.profession == "Thief" and self.level == 20):
            self.profession = "Assassin"

    def Apprentice(self):
        if (self.profession == "Apprentice" and self.level == 3):
            self.profession = "Warlock"
        if (self.profession == "Apprentice" and self.level == 10):
            self.profession = "Wizard"
        if (self.profession == "Apprentice" and self.level == 20):
            self.profession = "Head Mage"
        
    def Commoner(self):
        if (self.profession == "Commoner" and self.level == 3):
            self.profession = "Soldier"
        if (self.profession == "Commoner" and self.level == 10):
            self.profession = "Noble"
        if (self.profession == "Commoner" and self.level == 20):
            self.profession = "Great Lord"

    def Warrior(self):
        if (self.profession == "Warrior" and self.level == 0):
            self.profession = "Warrior"
        if (self.profession == "Warrior" and self.level == 3):
            self.profession = "Berserker"
        if (self.profession == "Warrior" and self.level == 10):
            self.profession = "Gladiator"
        if (self.profession == "Warrior" and self.level == 20):
            self.profession = "Slayer"

    def Archer(self):
        if (self.profession == "Archer" and self.level == 0):
           self.profession = "Archer"
        if (self.profession == "Archer" and self.level == 3):
            self.profession = "Hunter"
        if (self.profession == "Archer" and self.level == 10):
            self.profession = "Marksman"
        if (self.profession == "Archer" and self.level == 20):
            self.profession = "Ranger"
    
    def updateClass(self):
        Classes.Archer(self)
        Classes.Warrior(self)
        Classes.Commoner(self)
        Classes.Apprentice(self)
        Classes.Thief(self)
        Classes.Squire(self)
        return (self.profession)
