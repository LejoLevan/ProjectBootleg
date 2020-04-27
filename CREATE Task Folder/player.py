"""This is obviously the class that sets up the player
"""

class character:

    def __init__(self):
        #hp stats
        self.maxhp = 10
        self.hp = 10

        #attack stats
        self.physical_attack = 10
        self.magic_attack = 10

        #consume stats
        self.stamina = 10
        self.mana = 10

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
        self.crit_percent = 10
        self.crit_mult = 1.5
        self.luck = 10
        
        self.equipped_skills = []
        self.skills = []