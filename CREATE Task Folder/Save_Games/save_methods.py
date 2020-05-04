"""File contains functions that save
different data
"""
import json

def playerSave(player):
    """Function that will save data about
    the player

    Arguments:
        player  -- player will take a variable that refers to the
        character class
    """
    playerData = {
        'name': player.name,
        'profession': player.profession,

        'maxHP': player.maxhp,
        'hp': player.hp,

        'physicalAttack': player.physical_attack,
        'magicAttack': player.magic_attack,
        'speed': player.speed,

        'stamina': player.stamina,
        'maxStamina': player.stamina_max,
        'mana': player.mana,
        'maxMana': player.mana_max,

        'physicalDefense': player.physical_defense,
        'magicDefense': player.magic_defense,

        'fireResist': player.fire_resist,
        'poisonResist': player.poison_resist,
        'windResist': player.wind_resist,
        'waterResist': player.water_resist,
        'earthResist': player.earth_resist,

        'level': player.level,
        'exp': player.exp,
        'expCap': player.exp_cap,

        'accuracy': player.accuracy,
        'evasion': player.evasion,
        'criticalChance': player.crit_chance,
        'criticalMultiplier': player.crit_mult,
        'luck': player.luck,

        'equippedSkills': player.equipped_skills,
        'skills': player.skills,

        'weaponInventory': player.weapon_inventory,
        'armorInventory': player.armor_inventory,
        'buffInventory': player.buff_inventory,
        'questInventory': player.quest_inventory,
        'gold': player.gold
    }
    with open('CREATE Task Folder\Save_Games\player_logs.txt', 'w') as outfile:#pylint: disable = anomalous-backslash-in-string
        json.dump(playerData, outfile, indent=4)

def playerLoad():
    with open('CREATE Task Folder\Save_Games\player_logs.txt', 'r') as outfile:#pylint: disable = anomalous-backslash-in-string
        playerData = json.load(outfile)
    return playerData

def questLoad():
    with open('CREATE Task Folder\Save_Games\quest_logs.txt', 'r') as outfile:#pylint: disable = anomalous-backslash-in-string
        questData = json.load(outfile)
    return questData

def questSave(quest):
    """Function that will save data
    about quests

    Arguments:
        quest  -- quest will take a variable that refers to the Quest
        Checker class
    """
    questData = {
        'ongoingQuests': quest.ongoing_quests,
        'completedQuests': quest.completed_quests
    }
    with open('CREATE Task Folder\Save_Games\quest_logs.txt', 'w') as outfile:#pylint: disable = anomalous-backslash-in-string
        json.dump(questData, outfile, indent=4)
