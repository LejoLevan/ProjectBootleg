"""This is obviously the class that sets up the player
"""

from Leveling_System.Classes import Classes

class character:
    def __init__(self):
        #Info stats
        self.name = "Jack"
        self.icon = 'CREATE Task Folder\Image Assets\Player_Images\Commoner.png'
        
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
        self.poison_resist = 2
        self.water_resist = 2
        self.earth_resist = 2
        self.wind_resist = 2

        #level stats
        self.level = 0
        self.exp = 0
        self.exp_cap = 15

        #chance stats
        self.accuracy = 100
        self.evasion = 15
        self.crit_chance = 10
        self.crit_mult = 1.5
        self.luck = 10
        
        #skills stats
        self.equipped_skills = []
        self.skills = []

        #ally stats
        self.equipped_allies = []
        self.allies = []

        #misc stats
        self.total_inventory = 0
        self.weapon_inventory = ["a","f", "f", "f", "t"]
        self.armor_inventory = []
        self.buff_inventory = []
        self.misc_inventory = []
        self.quest_inventory = []
        self.gold = 10

        #flags
        self.bagCap = False
        self.combat = False

    def loadStats(self, stats):
        #Info stats
        self.name = stats['name']
        self.icon = stats['icon']

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
        self.wind_resist = stats['windResist']
        self.water_resist = stats['waterResist']
        self.earth_resist = stats['earthResist']
        self.poison_resist = stats['poisonResist']

        #level stats
        self.level = stats['level']
        self.exp = stats['exp']
        self.exp_cap = stats['expCap']

        #chance stats
        self.accuracy = stats['accuracy']
        self.evasion = stats['evasion']
        self.crit_chance = stats['criticalChance']
        self.crit_mult = stats['criticalMultiplier']
        self.luck = stats['luck']

        #skills stats
        self.equipped_skills = stats['equippedSkills']
        self.skills = stats['skills']

        #ally stats
        self.equipped_allies = stats['equippedAllies']
        self.allies = stats['allies']

        #misc Stats
        self.gold = stats['gold']
        self.weapon_inventory = stats['weaponInventory']
        self.armor_inventory = stats['armorInventory']
        self.buff_inventory = stats['buffInventory']
        self.misc_inventory = stats['miscInventory']
        self.quest_inventory = stats['questInventory']

    def update(self):
        self.profession = Classes.updateClass(self)
        self.checkBag()

    def appendInventory(self, inventory, item):
        if self.bagCap == False:
            if inventory == "Weapon Inventory" or "weapon inventory":
                self.weapon_inventory.append(item)
            elif inventory == "Armor Inventory" or "armor inventory":
                self.armor_inventory.append(item)
            elif inventory == "Buff Inventory" or "buff inventory":
                self.buff_inventory.append(item)
            elif inventory == "Misc Inventory" or "misc inventory":
                self.misc_inventory.append(item)
            elif inventory == "Quest Inventory" or "quest inventory":
                self.quest_inventory.append(item)

    def appendEquippedAlly(self, ally):
        if len(self.equipped_allies) <= 3:
            self.equipped_allies.append(ally)

    def checkBag(self):
        self.total_inventory = len(self.weapon_inventory) + len(self.armor_inventory) + len(self.buff_inventory) + len(self.misc_inventory)
        if self.total_inventory == 100:
            self.bagCap = True
