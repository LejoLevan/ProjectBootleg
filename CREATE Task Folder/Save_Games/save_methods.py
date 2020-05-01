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
        'posionResist': player.posion_resist,

        'level': player.level,
        'exp': player.exp,
        'expCap': player.exp_cap,

        'accuracy': player.accuracy,
        'criticalChance': player.crit_chance,
        'criticalMultiplier': player.crit_mult,
        'luck': player.luck,

        'equippedSkills': player.equipped_skills,
        'skills': player.skills,

        'gold': player.gold
    }
    with open('CREATE Task Folder\Save_Games\player_logs.txt', 'w') as outfile:
        json.dump(playerData, outfile, indent=4)

def playerLoad():
    with open('CREATE Task Folder\Save_Games\player_logs.txt', 'r') as outfile:
        playerData = json.load(outfile)
    return playerData

def questLoad():
    with open('quest_logs.txt', 'r') as outfile:
        questData = json.loads(outfile)
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
    with open('quest_logs.txt', 'w') as outfile:
        json.dump(questData, outfile)




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

