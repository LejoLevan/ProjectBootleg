"""This is obviously the class that sets up the player
"""
from save_methods import playerSave, playerLoad

class character:
    def __init__(self):
        #Info stats
        self.name = "fat"

        #class stats
        self.profession = "Commoner"

        #hp stats
        self.maxhp = 10
        self.hp = 10

        #attack stats
        self.physical_attack = 10
        self.magic_attack = 10
        self.speed = 10

        #consume stats
        self.stamina = 10
        self.stamina_max = 10
        self.mana = 10
        self.mana_max = 10

        #defense stats
        self.physical_defense = 10
        self.magic_defense = 10

        #resistance stats
        self.fire_resist = 5
        self.posion_resist = 5

        #level stats
        self.previous_level = -1
        self.level = 0
        self.exp = 0
        self.exp_cap = 100

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

if __name__ == '__main__':
    player = character()
    playerSave(player)
    player.loadStats(playerLoad())
    
    def allySave(ally):
    """Function that will save data about
    the ally

    Arguments:
        ally  -- ally will take a variable that refers to the
        character class
    """
    allyData = {
        ally.name, 'name': ally.name,

        ally.name, 'maxHP': ally.maxhp,
        ally.name, 'hp': ally.hp,

        ally.name, 'physicalAttack': ally.physical_attack,
        ally.name, 'magicAttack': ally.magic_attack,
        ally.name, 'speed': ally.speed,

        ally.name, 'stamina': ally.stamina,
        ally.name, 'maxStamina': ally.stamina_max,
        ally.name, 'mana': ally.mana,
        ally.name, 'maxMana': ally.mana_max,

        ally.name, 'physicalDefense': ally.physical_defense,
        ally.name, 'magicDefense': ally.magic_defense,

        ally.name, 'fireResist': ally.fire_resist,
        ally.name, 'posionResist': ally.posion_resist,

        ally.name, 'level': ally.level,
        ally.name, 'exp': ally.exp,
        ally.name, 'expCap': ally.exp_cap,

        ally.name, 'accuracy': ally.accuracy,
        ally.name, 'criticalChance': ally.crit_chance,
        ally.name, 'criticalMultiplier': ally.crit_mult,
        ally.name, 'luck': ally.luck,

        ally.name, 'equippedSkills': ally.equipped_skills,
        ally.name, 'skills': ally.skills,

    }
    with open('\CREATE Task Folder\Save_Games\ally_logs.txt', 'a') as outfile:
        json.dump(allyData, outfile, indent=4)

def allyLoad():
    with open('\CREATE Task Folder\Save_Games\ally_logs.txt', 'r') as outfile:
        allyData = json.load(outfile)
    return allyData