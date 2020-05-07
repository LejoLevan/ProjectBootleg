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
        player.exp_cap += 15
        player.previousLevel = player.previousLevel + 1
        upgradeProfession(player)
    if (player.level == 20):
        player.level = 20
        player.exp_cap = player.exp

def upgradeProfession(player):
    if (player.profession == "Thief" and self.level == 1):
        player.hp =
        player.maxhp =
        player.physical_attack =
        player.magic_attack =
        player.speed =
        player.stamina =
        player.stamina_max =
        player.mana =
        player.mana_max =
        player.physical_defense =
        player.magic_defense =
        player.fire_resist =
        player.poison_resist =
        player.accuracy =
        player.crit_percent =
        player.crit_mult =
        player.luck =
        elif (player.exp >= player.exp_cap):
            player.hp =
            player.maxhp =
            player.physical_attack =
            player.magic_attack =
            player.speed =
            player.stamina =
            player.stamina_max =
            player.mana =
            player.mana_max =
            player.physical_defense =
            player.magic_defense =
            player.fire_resist =
            player.poison_resist =
            player.accuracy =
            player.crit_percent =
            player.crit_mult =
            player.luck =
    if (player.profession == "Scoundrel" and self.level == 3):
        player.hp =
        player.maxhp =
        player.physical_attack =
        player.magic_attack =
        player.speed =
        player.stamina =
        player.stamina_max =
        player.mana =
        player.mana_max =
        player.physical_defense =
        player.magic_defense =
        player.fire_resist =
        player.poison_resist =
        player.accuracy =
        player.crit_percent =
        player.crit_mult =
        player.luck =
        elif (player.exp >= player.exp_cap):
            player.hp =
            player.maxhp =
            player.physical_attack =
            player.magic_attack =
            player.speed =
            player.stamina =
            player.stamina_max =
            player.mana =
            player.mana_max =
            player.physical_defense =
            player.magic_defense =
            player.fire_resist =
            player.poison_resist =
            player.accuracy =
            player.crit_percent =
            player.crit_mult =
            player.luck =
    if (player.profession == "Rogue" and self.level == 10):
        player.hp =
        player.maxhp =
        player.physical_attack =
        player.magic_attack =
        player.speed =
        player.stamina =
        player.stamina_max =
        player.mana =
        player.mana_max =
        player.physical_defense =
        player.magic_defense =
        player.fire_resist =
        player.poison_resist =
        player.accuracy =
        player.crit_percent =
        player.crit_mult =
        player.luck =
            elif (player.exp >= player.exp_cap):
            player.hp =
            player.maxhp =
            player.physical_attack =
            player.magic_attack =
            player.speed =
            player.stamina =
            player.stamina_max =
            player.mana =
            player.mana_max =
            player.physical_defense =
            player.magic_defense =
            player.fire_resist =
            player.poison_resist =
            player.accuracy =
            player.crit_percent =
            player.crit_mult =
            player.luck =
    if (player.profession == "Assassin" and self.level == 20):
        player.hp =
        player.maxhp =
        player.physical_attack =
        player.magic_attack =
        player.speed =
        player.stamina =
        player.stamina_max =
        player.mana =
        player.mana_max =
        player.physical_defense =
        player.magic_defense =
        player.fire_resist =
        player.poison_resist =
        player.accuracy =   
        player.crit_percent =
        player.crit_mult =
        player.luck =
        elif (player.exp >= player.exp_cap):
            player.hp =
            player.maxhp =
            player.physical_attack =
            player.magic_attack =
            player.speed =
            player.stamina =
            player.stamina_max =
            player.mana =
            player.mana_max =
            player.physical_defense =
            player.magic_defense =
            player.fire_resist =
            player.poison_resist =
            player.accuracy =
            player.crit_percent =
            player.crit_mult =
            player.luck =

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