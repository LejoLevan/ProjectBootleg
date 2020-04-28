"""This is obviously the class that sets up the player
"""

from Leveling_System.Classes import Classes

class character:
    def __init__(self):
        #Info stats
        self.name = ""

        #class stats
        self.profession = "Commoner"

        #hp stats
        self.maxhp = 10
        self.hp = 10

        #attack stats
        self.physical_attack = 10
        self.magic_attack = 10
        self.speed = 10

        #consume stats
        self.stamina = 10
        self.stamina_max = 10
        self.mana = 10
        self.mana_max = 10

        #defense stats
        self.physical_defense = 10
        self.magic_defense = 10

        #resistance stats
        self.fire_resist = 5
        self.posion_resist = 5

        #level stats
        self.previous_level = -1
        self.level = 0
        self.exp = 0
        self.exp_cap = 100

        #chance stats
        self.accuracy = 10
        self.crit_chance = 10
        self.crit_mult = 1.5
        self.luck = 10
        
        #skills stats
        self.equipped_skills = []
        self.skills = []

        self.gold = 10

    def loadStats(self, stats):
        #Info stats
        self.name = ""

        #class stats
        self.profession = ""

        #hp stats
        self.maxhp = 10
        self.hp = 10

        #attack stats
        self.physical_attack = 10
        self.magic_attack = 10

        #consume stats
        self.stamina = 10
        self.stamina_max = 10
        self.mana = 10
        self.mana_max = 10

        #defense stats
        self.physical_defense = 10
        self.magic_defense = 10

        #resistance stats
        self.fire_resist = 5
        self.posion_resist = 5

        #level stats
        self.level = 0
        self.exp = 0
        self.exp_cap = 100

        #chance stats
        self.crit_chance = 10
        self.crit_mult = 1.5
        self.luck = 10
        
        self.equipped_skills = []
        self.skills = []
    
    def update(self):
        self.profession = Classes(self)

