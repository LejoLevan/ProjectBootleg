import random
from items import weapon, armor, misc

class monster:
    def __init__(self, rpg):
        self.name = ""
        self.image = ""
        self.icon = ""
        self.profession = ""
        
        self.hp = 0
        self.maxhp = 0

        self.level = rpg.player.level + random.randrange(0, 3)
        self.exp = 0

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

        self.gold = 0
        self.intelligence = "Low"

        self.tierIIILoot = []
        self.tierIILoot = []
        self.tierILoot = []
    
    def goblin(self):
        CopperOre = misc()
        CopperOre.copper()

        CopperSword = weapon()
        CopperSword.copperSword()

        CopperArmor = armor()
        CopperArmor.copperArmor()

        self.name = random.choice(["Goblin Miner", "Goblin Footman"])

        if self.name == "Goblin Miner":
            self.image = "CREATE Task Folder\Image Assets\Enemy_images\Goblin Miner+.png"
            self.icon = "CREATE Task Folder\Image Assets\Enemy_images\Goblin Miner.png"
            
            self.maxhp = 35
            self.hp = 35

            self.physical_attack = 8
            self.speed = 7

            self.stamina = 30
            self.stamina_max = 30

            self.physical_defense = 2
            self.magic_defense  = 2

            self.fire_resist = 1
            self.earth_resist = 1
            self.wind_resist = 1 

            self.accuracy = 75
            self.evasion = 5
            self.crit_chance = 2.5
            self.crit_mult = 1.25
            self.luck = 10
            self.exp = 10

            self.gold = 5
            self.tierIILoot = [CopperOre, CopperOre]
            self.tierIIILoot = [CopperOre, CopperOre, CopperOre, CopperOre]
        
        elif self.name == "Goblin Footman":
            self.image = "CREATE Task Folder\Image Assets\Enemy_images\Goblin Footman+.png"
            self.icon = "CREATE Task Folder\Image Assets\Enemy_images\Goblin Footman.png"

            self.maxhp = 40
            self.hp = 40

            self.physical_attack = 10
            self.speed = 10

            self.stamina = 65
            self.stamina_max = 65

            self.physical_defense = 4
            self.magic_defense = 3

            self.poison_resist = 1
            self.water_resist = 2
            self.earth_resist = 2
            self.wind_resist = 2

            self.accuracy = 85
            self.evasion = 12
            self.crit_chance = 8
            self.crit_mult = 1.5
            self.luck = 5
            self.intelligence = "Medium"

            self.exp = 20
            self.gold = 3
            self.tierIILoot = [CopperSword]
            self.tierIIILoot = [CopperArmor]

        self.tierILoot = [CopperOre]




            



