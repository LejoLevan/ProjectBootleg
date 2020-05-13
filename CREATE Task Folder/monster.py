from items import weapon, armor

class monster:
    def __init__(self):
        bareFists = weapon()
        bareFists.bareFists()

        self.name = ""
        self.icon = ""
        
        self.hp = 0
        self.maxhp = 0

        self.weapon_equipped = bareFists

        self.physical_attack = 0
        self.magic_attack = 0
        self.speed = 0

        self.stamina = 0
        self.stamina_max = 0
        self.mana = 0
        self.mana_max = 0

        self.physical_defense = 0
        self.magic_defense = 0

        self.fire_resist = 0
        self.poison_resist = 0
        self.water_resist = 0
        self.earth_resist = 0
        self.wind_resist = 0

        self.accuracy = 0
        self.evasion = 0
        self.crit_chance = 0
        self.crit_mult = 0
        self.luck = 0
