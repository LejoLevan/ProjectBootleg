import random

class weapon:
    def __init__(self):
        self.name = ""
        self.icon = ""
        self.tag = "Weapon"
        self.physical_attack = 0
        self.magic_attack = 0
        self.speed = 0
        self.info = ""
        self.max_durability = 0
        self.durability = 0
        self.destructible = True

    def copperSword(self):
        self.name = "Copper Sword"
        self.icon = "CREATE Task Folder\Image Assets\Weapon_Images\CopperSword.png"
        self.physical_attack = random.choice([2, 3])
        self.max_durability = 10
        self.durability = 10
        self.info = "CREATE Task Folder\Image Assets\Weapon_Images\Copper Sword Info.png"
    
    def bareFists(self):
        self.name = "Bare Fists"
        self.physical_attack = random.choice([0, 1])
        self.destructible = False

class misc:
    def __init__(self):
        self.name = ""
        self.tag = "Misc"
        self.icon = ""
        self.info = ""
    
    def copper(self):
        self.name = "Copper"
        self.icon = "CREATE Task Folder\Image Assets\Material_Images\CopperOre.png"
        self.info = "CREATE Task Folder\Image Assets\Material_Images\Copper Ore Info.png"
class armor:
    def __init__(self):
        self.name = ""
        self.tag = "Armor"
        self.info = ""
        self.icon = ""

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

        self.destructible = True
    
    def naked(self):
        self.name = "Naked"
        self.speed = 2
        self.destructible = False
    
    def copperArmor(self):
        self.name = "Copper Armor"
        self.info = "CREATE Task Folder\Image Assets\Armor_Images\Copper Armor Info.png"
        self.icon = "CREATE Task Folder\Image Assets\Armor_Images\CopperArmor.png"
        self.physical_defense = 2
        self.magic_defense = 1
        self.fire_resist = 1
        self.destructible = False

class buffs:
    def __init__(self):
        self.name = ""
        self.icon = ""
        self.info = ""
        self.tag = "Buff"

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
    
    def healthPotion (self):
        self.name = "Health Potion"
        self.icon = "CREATE Task Folder\Image Assets\Item_Images\HealthPotion.png"
        self.info = "CREATE Task Folder\Image Assets\Item_Images\Health Potion Info.png"
        self.hp = 25
