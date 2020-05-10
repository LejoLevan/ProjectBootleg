from npc.py import ally
from player.py import character
import random

def level(player):
    print("Level:",player.level)
    print("Current Experience:",player.exp+"/"+player.exp_cap)
    print("Experience Until Next Level:",player.exp_cap-player.exp)
    
def NextLevel(player):
    while (player.exp >= player.exp_cap):
        player.level = player.level + 1
        player.exp = player.exp-player.exp_cap
        player.exp_cap += 15
        player.previousLevel = player.previousLevel + 1
        upgradeProfession(player)
    if (player.level == 20):
        player.level = 20
        player.exp_cap = player.exp

def upgradeProfession(player):
    if (player.profession == "Thief"):
        player.hp = player.hp + random.choice([1, 2, 3, 4, 5]) 
        player.maxhp = player.maxhp + random.choice([1, 2, 3, 4, 5]) 
        player.physical_attack = player.physical_attack + random.choice([1, 2, 3])
        player.magic_attack = player.magic_attack + 0
        player.speed = player.speed + random.choice([1, 2, 3])
        player.stamina = player.stamina + random.choice([1, 2, 3])
        player.stamina_max = player.stamina_max + random.choice([1, 2, 3, 4, 5])
        player.mana = player.mana + 0
        player.mana_max = player.mana_max + 0
        player.physical_defense = player.physical_defense + random.choice([1, 2])
        player.magic_defense = player.magic_defense + random.choice([0, 1])
        player.fire_resist = player.fire_resist + random.choice([1, 2])
        player.poison_resist = player.poison_resist + random.choice([1, 2])
        player.accuracy = player.accuracy + random.choice([1, 2])
        player.crit_percent = player.crit_percent + random.choice([1, 2, 3])
        player.crit_mult = player.crit_mult + random.choice([1, 2])
        player.luck = player.luck + random.choice([1, 2, 3])
    if (player.profession == "Scoundrel"):
        player.hp = player.hp + random.choice([1, 2, 3, 4, 5]) 
        player.maxhp = player.hp + random.choice([1, 2, 3, 4, 5]) 
        player.physical_attack = player.physical_attack + random.choice([1, 2, 3])
        player.magic_attack = player.magic_attack + 0
        player.speed = player.speed + random.choice([1, 2, 3])
        player.stamina = player.stamina + random.choice([1, 2, 3])
        player.stamina_max = player.stamina + random.choice([1, 2, 3, 4, 5])
        player.mana = player.mana + 0
        player.mana_max = player.mana_max + 0
        player.physical_defense = player.physical_defense + random.choice([1, 2])
        player.magic_defense = player.magic_defense + random.choice([0, 1])
        player.fire_resist = player.fire_resist + random.choice([1, 2])
        player.poison_resist = player.poison_resist random.choice([1, 2])
        player.accuracy = player.accuracy + random.choice([1, 2])
        player.crit_percent = player.crit_percent + random.choice([1, 2, 3])
        player.crit_mult = player.crit_mult + random.choice([1, 2])
        player.luck = player.luck + random.choice([1, 2, 3])
    if (player.profession == "Rogue"):
        player.hp = player.hp + random.choice([1, 2, 3, 4, 5]) 
        player.maxhp = player.hp + random.choice([1, 2, 3, 4, 5]) 
        player.physical_attack = player.physical_attack + random.choice([1, 2, 3])
        player.magic_attack = player.magic_attack + 0
        player.speed = player.speed + random.choice([1, 2, 3])
        player.stamina = player.stamina + random.choice([1, 2, 3])
        player.stamina_max = player.stamina + random.choice([1, 2, 3, 4, 5])
        player.mana = player.mana + 0
        player.mana_max = player.mana_max + 0
        player.physical_defense = player.physical_defense + random.choice([1, 2])
        player.magic_defense = player.magic_defense + random.choice([0, 1])
        player.fire_resist = player.fire_resist + random.choice([1, 2])
        player.poison_resist = player.poison_resist random.choice([1, 2])
        player.accuracy = player.accuracy + random.choice([1, 2])
        player.crit_percent = player.crit_percent + random.choice([1, 2, 3])
        player.crit_mult = player.crit_mult + random.choice([1, 2])
        player.luck = player.luck + random.choice([1, 2, 3])
    if (player.profession == "Assassin"):
        player.hp = player.hp + random.choice([1, 2, 3, 4, 5, 6, 7]) 
        player.maxhp = player.hp + random.choice([1, 2, 3, 4, 5]) 
        player.physical_attack = player.physical_attack + random.choice([1, 2, 3])
        player.magic_attack = player.magic_attack + 0
        player.speed = player.speed + random.choice([1, 2, 3])
        player.stamina = player.stamina + random.choice([1, 2, 3])
        player.stamina_max = player.stamina + random.choice([1, 2, 3, 4, 5])
        player.mana = player.mana + 0
        player.mana_max = player.mana_max + 0
        player.physical_defense = player.physical_defense + random.choice([1, 2])
        player.magic_defense = player.magic_defense + random.choice([0, 1])
        player.fire_resist = player.fire_resist + random.choice([1, 2])
        player.poison_resist = player.poison_resist random.choice([1, 2])
        player.accuracy = player.accuracy + random.choice([1, 2])
        player.crit_percent = player.crit_percent + random.choice([1, 2, 3, 4, 5, 6])
        player.crit_mult = player.crit_mult + random.choice([1, 2, 3, 4])
        player.luck = player.luck + random.choice([1, 2, 3])

def updateAlly(ally, level, player):
    if ():
        ally.level = player.level
        ally.hp = player.hp
        ally.maxhp = .player.maxhp
        ally.physical_attack = player.physical_attack
        ally.magic_attack = player.magic_attack
        ally.speed = player.speed
        ally.stamina = player.stamina
        ally.stamina_max = player.stamina_max
        ally.mana = player.mana
        ally.mana_max = player.mana_max
        ally.physical_defense = player.physical_defense
        ally.magic_defense = player.magic_defense
        ally.fire_resist = player.fire_resist
        ally.poison_resist = player.poison_resist
        ally.accuracy = player.accuracy
        ally.crit_percent = player.crit_percent
        ally.crit_mult = player.crit_mult
        ally.luck = player.luck