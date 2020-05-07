class weapon:
    def __init__(self, stats):
        self.name = stats['name']
        self.physical_attack = stats['physical_attack']
        self.magic_attack = stats["magic_attack"]
        self.speed = stats["speed"]


class armor:
    def __init__(self, stats):
        self.name = stats["name"]
        self.physical_defense = stats["physical_defense"]
        self.magic_defense = stats["magic_defense"]

        self.fire_resist = stats["fire_resist"]
        self.poison_resist = stats["poison_resist"]
        self.water_resist = stats["water_resist"]
        self.earth_resist = stats["earth_resist"]
        self.wind_resist = stats["wind_resist"]
        
        self.speed = stats["speed"]
        self.stamina_max = stats["stamina_max"]
        self.mana_max = stats["mana_max"]

    def equip():
        

class buffs:
    def __init__(self, stats):
        #hp stats
        self.maxhp = stats["maxhp"]
        self.hp = stats["hp"]

        #attack stats
        self.physical_attack = stats["physical_attack"]
        self.magic_attack = stats["magic_attack"]
        self.speed = stats["speed"]

        #consume stats
        self.stamina = stats["stamina"]
        self.stamina_max = stats["stamina_max"]
        self.mana = stats["mana"]
        self.mana_max = stats["mana_max"]

        #defense stats
        self.physical_defense = stats["physical_defense"]
        self.magic_defense = stats["magic_defense"]

        #resistance stats
        self.fire_resist = stats["fire_resist"]
        self.poison_resist = stats["poison_resist"]
        self.water_resist = stats["water_resist"]
        self.earth_resist = stats["earth_resist"]
        self.wind_resist = stats["wind_resist"]

        #chance stats
        self.accuracy = stats["accuracy"]
        self.evasion = stats["evasion"]
        self.crit_chance = stats["crit_chance"]
        self.crit_mult = stats["crit_mult"]
        self.luck = stats["luck"]
