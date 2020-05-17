import random
import pygame
import sys

from monster import monster

def battle(rpg, location):
    rpg.battle_active = True
    enemy = monster(rpg)
    rpg.combatGUI.enemy = enemy

    if location == "Village":
        enemyList = [enemy.goblin()]
        random.choice(enemyList)
        rpg.combatGUI.background.image = pygame.image.load('CREATE Task Folder\Image Assets\Battle_Images\Village Forest.png')
    
    battleOver = False
    while rpg.combatGUI.battleOver == False:
        if whoFirst(rpg, enemy) == "Player":
            playerTurn(rpg, enemy)
            checkHealths(rpg, enemy)
            monsterTurn(rpg, enemy)
            checkHealths(rpg, enemy)
        else:
            monsterTurn(rpg, enemy)
            checkHealths(rpg, enemy)
            playerTurn(rpg, enemy)
            checkHealths(rpg, enemy)
    rpg.battle_active = False

def whoFirst(rpg, enemy):
    if rpg.player.stamina == 0:
        return("Monster")
    elif enemy.stamina == 0:
        return("Player")
    else:
        playerSpeed = rpg.player.speed + rpg.player.weapon.speed + rpg.player.armor.speed
        if playerSpeed > enemy.speed:
            return("Player")
        elif playerSpeed < enemy.speed:
            return("Monster")
        else:
            if rpg.player.luck <= random.randrange(0, 100):
                return("Player")
            else:
                return("Monster")

def playerTurn(rpg, enemy):
    while rpg.combatGUI.attack == False:
        rpg._check_events()
        if rpg.game_active:
            rpg.template.update()
            rpg.player.update()
        rpg._update_screen()
    if rpg.combatGUI.attack == True:
        attack(rpg, enemy, "Player")
        rpg.combatGUI.attack = False
    elif rpg.combatGUI.defend == True:
        defend(rpg, enemy, "Player")
    elif rpg.combatGUI.rest == True:
        rest(rpg, enemy, "Player")
    elif rpg.combatGUI.use == True:
        pass 

def checkHealths(rpg, enemy):
    if rpg.player.hp <= 0:
        battleOver = True
        try:
            rpg.player.exp -= (rpg.player.exp*.2)
        except Exception:
            pass
        try:
            rpg.player.gold -= (rpg.player.exp)
        except Exception:
            pass
        if random.randrange(0, 100) >= 85:
            inventory = random.choice(["Weapon Inventory", "Armor Inventory"])
            if inventory == "Weapon Inventory":
                item = rpg.player.weapon
            else:
                item = rpg.player.armor
            rpg.player.deleteInventory(inventory, item)
    if enemy.hp <= 0:
        print("Allo")
        rpg.combatGUI.battleOver = True
        loot(rpg, enemy)

def loot(rpg, enemy):
    pass

def monsterTurn(rpg, enemy):
    pass


def attack(rpg, enemy, who):
    if who == "Player":
        if rpg.player.profession == "Apprentice" or rpg.player.profession == "Warlock" or rpg.player.profession == "Wizard":
            print("Huhfdgs")
            if rpg.player.mana >= rpg.player.magic_attack:
                if random.randrange(0, 100) <= rpg.player.crit_chance:
                    enemy.hp -= rpg.player.magic_attack * rpg.player.crit_mult + enemy.magic_defense
                    rpg.player.mana -= rpg.player.magic_attack
                else:
                    enemy.hp -= rpg.player.magic_attack + enemy.magic_defense
                    rpg.player.mana -= rpg.player.magic_attack
            else:
                rpg.player.hp -= (rpg.player.maxhp * (random.randrange(5, 10)/100))
        else:
            if rpg.player.stamina >= rpg.player.physical_attack:
                if random.randrange(0, 100) <= rpg.player.crit_chance:
                    enemy.hp -= rpg.player.physical_attack * rpg.player.crit_mult + enemy.physical_defense
                    rpg.player.stamina -= rpg.player.physical_attack
                else:
                    enemy.hp -= rpg.player.physical_attack + enemy.physical_defense
                    rpg.player.stamina -= rpg.player.physical_attack
            else:
                rpg.player.hp -= (rpg.player.maxhp * random.randrange((5, 10)/100))

    if who == "Monster":
        if enemy.profession == "Mage":
            if enemy.mana >= enemy.magic_attack:
                if random.randrange(0, 100) <= enemy.crit_chance:
                    rpg.player.hp -= enemy.magic_attack * enemy.crit_mult + rpg.player.magic_defense
                    enemy.mana -= enemy.magic_attack
                else:
                    rpg.player.hp -= enemy.magic_attack + rpg.player.magic_defense
                    enemy.mana -= enemy.magic_attack
            else:
                enemy.hp -= (enemy.maxhp * random.randrange((5, 10)/100))
        else:
            if enemy.stamina >= enemy.physical_attack:
                if random.randrange(0, 100) <= enemy.crit_chance:
                    rpg.player.hp -= enemy.physical_attack * enemy.crit_mult + rpg.player.physical_defense
                    enemy.stamina -= enemy.physical_attack
                else:
                    rpg.player.hp -= enemy.physical_attack + rpg.player.physical_defense
                    enemy.stamina -= enemy.physical_attack
            else:
                enemy.hp -= (enemy.maxhp * random.randrange((5, 10)/100))



def defend(rpg, enemy, who):
    pass


def rest(rpg, enemy, who):
    if who == "Player":
        if rpg.player.stamina >= 10:
            rpg.player.hp += (rpg.player.maxhp * random.randrange((10, 25)/100))
            rpg.player.stamina -= 10
        else: 
            rpg.player.hp -= (rpg.player.maxhp * random.randrange((10, 25)/100))

    if who == "Monster":
        if enemy.stamina >=10:
            enemy.hp += (enemy.maxhp * random.randrange((10, 25)/100))
            enemy.stamina -= 10
        else:
            enemy.hp -= (enemy.maxhp * random.randrange((10, 25)/100))

