from npc.py import ally
from player.py import character
def level(player):
    print("Level:",player.level)
    print("Current Experience:",player.exp+"/"+player.exp_cap)
    print("Experience Until Next Level:",player.exp_cap-player.exp)
    
def NextLevel(player):
    while (player.exp >= player.exp_cap):
        player.level = player.level + 1
        player.exp = player.exp-player.exp_cap
        print("You are now level:", player.level)
        player.exp_cap += 100
        print("The new exp cap is now:", player.exp_cap)
        player.previousLevel = player.previousLevel + 1
        upgradeStats(player)
    if (player.level == 20):
        player.level = 20
        print("You are now max level:")
        player.exp_cap = player.exp

def upgradeStats(player):
    if (player.profession == "Thief"):

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