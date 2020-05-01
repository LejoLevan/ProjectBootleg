class vendor:
    def __init__(self, name, occupation):
        self.name = name
        self.occupation = occupation
        self.inventory = []
        self.forge = []

    def sell(self, item):
        


def blacksmith1():
    blacksmith = vendor("Bob", "blacksmith")
    blacksmith.inventory.append("") #put items 
    #print(")

def alchemist1():
    alchemist = vendor("Dave", "alchemist")
    alchemist.inventory.append("health potion,", "mana potion", )#add more potions

def beginnerShop():
    shop = vendor("Jack","beginnerShop")
    shop.inventory.append("wooden sword", "bone knife", "wooden bow", "tree stick", "rusty hatchet", "Rusty Great Sword")


class ally:
    def __init__(self, name, hp, maxhp, physical_attack, magic_attack, speed, stamina, stamina_max, mana, mana_max, physical_defense, magic_defense, fire_resist, poison_resist,
     level, exp, exp_cap, accuracy, crit_percent, crit_mult, luck):
        #hp stats
        self.name = name 
        self.maxhp = maxhp
        self.hp = hp

        #attack stats
        self.physical_attack = physical_attack
        self.magic_attack = magic_attack
        self.speed = speed

        #consume stats
        self.stamina = stamina
        self.stamina_max = stamina_max
        self.mana = mana
        self.mana_max = mana_max

        #defense stats
        self.physical_defense = physical_defense
        self.magic_defense = magic_defense

        #resistance stats
        self.fire_resist = fire_resist
        self.posion_resist = poison_resist

        #level stats
        self.level = level
        self.exp = exp
        self.exp_cap = exp_cap

        #chance stats
        self.accuracy = accuracy
        self.crit_chance = crit_percent
        self.crit_mult = crit_mult
        self.luck = luck
        
        #skills
        self.equipped_skills = []
        self.skills = []

        #def updateAlly():

        def allyGainHealth(self,x):
            self.hp = self.hp + x
            return self.hp
        
        def allyLoseHealth(self,x)
            self.hp = self.hp - x
            return self.hp
        
        def allyGainMaxHealth(self,x)
            self.maxhp = self.maxhp + x
            return self.maxhp


def allyPhillip():
    phillip = ally("Phillip", 150, 150, 5, 1, 5, 100, 100, 30, 30, 3, 3, 5, 5, 1, 0, 15, 10, 5, 1.2, 5)

