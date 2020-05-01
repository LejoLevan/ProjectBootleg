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
        self.maxhp = 100
        self.hp = 100

        #attack stats
        self.physical_attack = 5
        self.magic_attack = 5
        self.speed = 5

        #consume stats
        self.stamina = 100
        self.stamina_max = 100
        self.mana = 100
        self.mana_max = 100

        #defense stats
        self.physical_defense = 5
        self.magic_defense = 5

        #resistance stats
        self.fire_resist = 2
        self.posion_resist = 2

        #level stats
        self.level = 0
        self.exp = 0
        self.exp_cap = 15

        #chance stats
        self.accuracy = 10
        self.crit_chance = 10
        self.crit_mult = 1.5
        self.luck = 10
        
        #skills stats
        self.equipped_skills = []
        self.skills = []

        self.gold = 10

        self.combat = False

    def loadStats(self, stats):
        #Info stats
        self.name = stats['name']

        #class stats
        self.profession = stats['profession']

        #hp stats
        self.maxhp = stats['maxHP']
        self.hp = stats['hp']

        #attack stats
        self.physical_attack = stats['physicalAttack']
        self.magic_attack = stats['magicAttack']
        self.speed = stats['speed']

        #consume stats
        self.stamina = stats['stamina']
        self.stamina_max = stats['maxStamina']
        self.mana = stats['mana']
        self.mana_max = stats['maxMana']

        #defense stats
        self.physical_defense = stats['physicalDefense']
        self.magic_defense = stats['magicDefense']

        #resistance stats
        self.fire_resist = stats['fireResist']
        self.posion_resist = stats['posionResist']

        #level stats
        self.previous_level = stats['previousLevel']
        self.level = stats['level']
        self.exp = stats['exp']
        self.exp_cap = stats['expCap']

        #chance stats
        self.accuracy = stats['accuracy']
        self.crit_chance = stats['criticalChance']
        self.crit_mult = stats['criticalMultiplier']
        self.luck = stats['luck']

        self.equipped_skills = stats['equippedSkills']
        self.skills = stats['skills']

        self.gold = stats['gold']

    def update(self):
        self.profession = Classes.updateClass(self)
