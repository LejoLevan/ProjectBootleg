import random

class weapon:
    def __init__(self):
        self.name = ""
        self.physical_attack = 0
        self.magic_attack = 0
        self.speed = 0

    def copperSword(self):
        self.name = "Copper Sword"
        self.physical_attack = random.choice([1, 3])
        self.magic_attack = 0
        self.speed = 0

class armor:
    def __init__(self):
        self.name = ""
        self.physical_defense = 0
        self.magic_defense = 0

        self.fire_resist = 0
        self.poison_resist = 0
        self.water_resist = 0
        self.earth_resist = 0
        self.wind_resist = 0
        
        self.speed = 0
        self.stamina_max = 0
        self.mana_max = 0
        

class buffs:
    def __init__(self):
        #hp stats
        self.maxhp = 0
        self.hp = 0

        #attack stats
        self.physical_attack = 0
        self.magic_attack = 0
        self.speed = 0

        #consume stats
        self.stamina = 0
        self.stamina_max = 0
        self.mana = 0
        self.mana_max = 0

        #defense stats
        self.physical_defense = 0
        self.magic_defense = 0

        #resistance stats
        self.fire_resist = 0
        self.poison_resist = 0
        self.water_resist = 0
        self.earth_resist = 0
        self.wind_resist = 0

        #chance stats
        self.accuracy = 0
        self.evasion = 0
        self.crit_chance = 0
        self.crit_mult = 0
        self.luck = 0
