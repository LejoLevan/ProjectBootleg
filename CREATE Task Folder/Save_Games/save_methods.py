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
    playerData = {}
    playerData['player'] = []
    playerData['player'].append({
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

        'previousLevel': player.previous_level,
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
    })
    with open('player_logs.txt', 'w') as outfile:
        json.dump(playerData, outfile)

def playerLoad():
    with open('player_logs.txt', 'r') as outfile:
        playerData = json.loads(outfile)
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
    questData = {}
    questData['quests'] = []
    questData['quests'].append({
        'ongoingQuests': quest.ongoing_quests,
        'completedQuests': quest.completed_quests
    })
    with open('quest_logs.txt', 'w') as outfile:
        json.dump(questData, outfile)


def allySave (ally):
    allyData = {}
    allyData['ally'] = []
    allyData['ally'].append({
        'name': ally.name,
        'profession': ally.profession,

        'maxHP': ally.maxhp, 
        'hp': ally.hp,

        'physicalAttack': ally.physical_attack,
        'magicAttack': ally.magic_attack,

        'stamina': ally.stamina
    })