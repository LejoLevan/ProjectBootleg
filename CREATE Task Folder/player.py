"""This is obviously the class that sets up the player
"""

from Leveling_System.Classes import Classes
from items import weapon, buffs, armor


class character:
    def __init__(self):
        CopperArmor = armor()
        CopperArmor.copperArmor()

        CopperSword = weapon()
        CopperSword.copperSword()

        HealthPotion = buffs()
        HealthPotion.healthPotion()

        self.bareFists = weapon()
        self.bareFists.bareFists()

        self.naked = armor()
        self.naked.naked()

        #Info stats
        self.name = "Jack"
        self.icon = 'CREATE Task Folder\Image Assets\Player_Images\Commoner.png'

        #equip stats
        self.weapon = CopperSword
        self.armor = CopperArmor
        
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
        self.accuracy = 75
        self.evasion = 15
        self.crit_chance = 10
        self.crit_mult = 1.5
        self.luck = 00
        
        #skills stats
        self.equipped_skills = []
        self.skills = []

        #ally stats
        self.equipped_allies = []
        self.allies = []

        #misc stats
        self.total_inventory = 0

        self.weapons = [CopperSword.name, CopperSword.name]
        self.weapon_inventory = [CopperSword, CopperSword]

        self.armors = [CopperArmor.name]
        self.armor_inventory = [CopperArmor]

        self.buffs = [HealthPotion.name, HealthPotion.name]
        self.buff_inventory = [HealthPotion, HealthPotion]

        self.miscs = []
        self.misc_inventory = []

        self.quest_items = []
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

        self.weapons = stats['weapons']
        self.weapon_inventory = stats['weaponInventory']

        self.armors = stats['armors']
        self.armor_inventory = stats['armorInventory']

        self.buffs = stats['buffs']
        self.buff_inventory = stats['buffInventory']

        self.miscs = ['miscs']
        self.misc_inventory = stats['miscInventory']

        self.quest_items = stats['questItems']
        self.quest_inventory = stats['questInventory']

    def update(self):
        self.profession = Classes.updateClass(self)
        self.checkBag()
    
    def appendInventory(self, inventory, item):
        if self.bagCap == False:
            if inventory == "Weapon Inventory":
                try:
                    self.weapon_inventory.append(item)
                    self.weapons.append(item.name)
                    self.weapon_inventory.sort()
                    self.weapons.sort()
                except:
                    pass
            elif inventory == "Armor Inventory":
                try:
                    self.armor_inventory.append(item)
                    self.armors.append(item.name)
                    self.armor_inventory.sort()
                    self.armors.sort()
                except:
                    pass
            elif inventory == "Buff Inventory":
                try:
                    self.buff_inventory.append(item)
                    self.buffs.append(item.name)
                    self.buff_inventory.sort()
                    self.buffs.sort()
                except:
                    pass
            elif inventory == "Misc Inventory":
                try:
                    self.misc_inventory.append(item)
                    self.miscs.append(item.name)
                    self.misc_inventory.sort()
                    self.miscs.sort()
                except:
                    pass
            elif inventory == "Quest Inventory":
                try:
                    self.quest_inventory.append(item)
                    self.quest_items.append(item.name)
                    self.quest_inventory.sort()
                    self.quest_items.sort()
                except:
                    pass
    
    def deleteInventory(self, inventory, item):
        if inventory == "Weapon Inventory":
            try:
                self.weapon_inventory.remove(item)
                self.weapons.remove(item.name)
                self.weapon_inventory.sort()
                self.weapons.sort()
                if self.weapon.name == item.name and item.name not in self.weapons:
                    self.weapon = self.bareFists
            except:
                pass
        if inventory == "Armor Inventory":
            try:
                self.armor_inventory.remove(item)
                self.armors.remove(item.name)
                self.armor_inventory.sort()
                self.armors.sort()
                if self.armor.name == item.name and item.name not in self.armors:
                    self.armor = self.naked
            except:
                pass
        if inventory == "Buff Inventory":
            try:
                self.buff_inventory.remove(item)
                self.buffs.remove(item.name)
                self.buff_inventory.sort()
                self.buffs.sort()
            except:
                pass
        if inventory == "Misc Inventory":
            try:
                self.misc_inventory.remove(item)
                self.miscs.remove(item.name)
                self.misc_inventory.sort()
                self.miscs.sort()
            except:
                pass
        if inventory == "Quest Inventory":
            try:
                self.quest_inventory.remove(item)
                self.quest_items.remove(item.name)
                self.quest_inventory.sort()
                self.quest_items.sort()
            except:
                pass

    def useBuff(self, item):
        self.maxhp = self.maxhp + item.maxhp
        self.physical_attack = self.physical_attack + item.physical_attack
        self.magic_attack = self.magic_attack + item.magic_attack
        self.speed = self.speed + item.speed
        self.stamina_max = self.stamina_max + item.stamina_max 
        self.mana_max = self.mana_max + item.mana_max
        self.physical_defense = self.physical_defense + item.physical_defense
        self.magic_defense = self.magic_defense + item.magic_defense
        self.fire_resist = self.fire_resist + item.fire_resist
        self.poison_resist = self.poison_resist + item.poison_resist
        self.water_resist = self.water_resist + item.water_resist
        self.earth_resist = self.earth_resist + item.earth_resist
        self.wind_resist = self.wind_resist + item.wind_resist
        self.accuracy = self.accuracy + item.accuracy
        self.evasion = self.evasion + item.evasion
        self.crit_chance = self.crit_chance + item.crit_chance
        self.luck = self.luck + item.crit_chance  
        if self.hp + item.hp < self.maxhp:
            self.hp = self.hp + item.hp
        else: 
            self.hp = self.maxhp
        if self.mana + item.mana < self.mana_max:
            self.mana = self.mana + item.mana
        else:
            self.mana = self.mana_max
        if self.stamina + item.stamina < self.stamina_max:
            self.stamina = self.stamina + item.stamina
        else:
            self.stamina = self.stamina_max
        self.deleteInventory("Buff Inventory", item)

    def appendEquippedAlly(self, ally):
        if len(self.equipped_allies) <= 3:
            self.equipped_allies.append(ally)

    def checkBag(self):
        self.total_inventory = len(self.weapon_inventory) + len(self.armor_inventory) + len(self.buff_inventory) + len(self.misc_inventory)
        if self.total_inventory == 100:
            self.bagCap = True
