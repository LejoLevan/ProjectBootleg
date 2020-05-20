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
    rpg.combatGUI.battleOver = False

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
    while rpg.combatGUI.attack == False and rpg.combatGUI.defend == False and rpg.combatGUI.rest == False and rpg.combatGUI.use == False:
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
        rpg.combatGUI.defend = False
    elif rpg.combatGUI.rest == True:
        rest(rpg, enemy, "Player")
        rpg.combatGUI.rest = False
    elif rpg.combatGUI.use == True:
        pass 
        rpg.combatGUI.use = False

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
        rpg.combatGUI.battleOver = True
        loot(rpg, enemy)

def monsterTurn(rpg, enemy):
    pass

def loot(rpg, enemy):
    if(random.randrange(0,100) <= rpg.player.luck):
        for item in enemy.tierILoot:
            if(item.tag == "Weapon"):
                rpg.player.appendInventory("Weapon Inventory", item)
            if(item.tag == "Armor"):
                rpg.player.appendInventory("Armor Inventory", item)
            if(item.tag == "Misc"):
                rpg.player.appendInventory("Misc Inventory", item)
            if(item.tag == "Buff"):
                rpg.player.appendInventory("Buff Inventory", item)
        if(random.randrange(0,100) <= rpg.player.luck):
            for item in enemy.tierIILoot:
                if(item.tag == "Weapon"):
                    rpg.player.appendInventory("Weapon Inventory", item)
                if(item.tag == "Armor"):
                    rpg.player.appendInventory("Armor Inventory", item)
                if(item.tag == "Misc"):
                    rpg.player.appendInventory("Misc Inventory", item)
                if(item.tag == "Buff"):
                    rpg.player.appendInventory("Buff Inventory", item)
        if(random.randrange(0,100) <= rpg.player.luck):
            for item in enemy.tierIIILoot:
                if(item.tag == "Weapon"):
                    rpg.player.appendInventory("Weapon Inventory", item)
                if(item.tag == "Armor"):
                    rpg.player.appendInventory("Armor Inventory", item)
                if(item.tag == "Misc"):
                    rpg.player.appendInventory("Misc Inventory", item)
                if(item.tag == "Buff"):
                    rpg.player.appendInventory("Buff Inventory", item)
    if(random.randrange(0,100) <= rpg.player.luck):
        rpg.player.gold += enemy.gold * 1.5
    else:
        rpg.player.gold += enemy.gold

def attack(rpg, enemy, who):
    if who == "Player":
        if rpg.player.profession == "Apprentice" or rpg.player.profession == "Warlock" or rpg.player.profession == "Wizard":
            if rpg.player.mana >= rpg.player.magic_attack:
                if random.randrange(0, 100) <= rpg.player.crit_chance:
                    enemy.hp -= (rpg.player.magic_attack + rpg.player.weapon.magic_attack) * rpg.player.crit_mult + enemy.magic_defense
                    rpg.player.mana -= rpg.player.magic_attack
                else:
                    enemy.hp -= rpg.player.magic_attack + rpg.player.weapon.magic_attack + enemy.magic_defense
                    rpg.player.mana -= rpg.player.magic_attack
            else:
                rpg.player.hp -= ((rpg.player.maxhp * random.randrange(5, 10))/100)
        else:
            if rpg.player.stamina >= rpg.player.physical_attack:
                if random.randrange(0, 100) <= rpg.player.crit_chance:
                    enemy.hp -= (rpg.player.physical_attack + rpg.player.weapon.physical_attack) * rpg.player.crit_mult + enemy.physical_defense
                    rpg.player.stamina -= rpg.player.physical_attack
                else:
                    enemy.hp -= rpg.player.physical_attack + rpg.player.weapon.physical_attack + enemy.physical_defense
                    rpg.player.stamina -= rpg.player.physical_attack
            else:
                rpg.player.hp -= ((rpg.player.maxhp * random.randrange(5, 10))/100)

    if who == "Monster":
        playerPhysicalDefense = rpg.player.physical_defense
        playerMagicDefense = rpg.player.magic_defense
        if rpg.combatGUI.increaseDefend == True:
            playerPhysicalDefense += rpg.player.physical_defense * 0.1
            playerMagicDefense += rpg.player.magic_defense * 0.1
            
        if enemy.profession == "Mage":
            if enemy.mana >= enemy.magic_attack:
                if random.randrange(0, 100) <= enemy.crit_chance:
                    rpg.player.hp -= enemy.magic_attack * enemy.crit_mult + playerMagicDefense
                    enemy.mana -= enemy.magic_attack
                else:
                    rpg.player.hp -= enemy.magic_attack + playerMagicDefense
                    enemy.mana -= enemy.magic_attack
            else:
                enemy.hp -= ((enemy.maxhp * random.randrange(5, 10))/100)
        else:
            if enemy.stamina >= enemy.physical_attack:
                if random.randrange(0, 100) <= enemy.crit_chance:
                    rpg.player.hp -= enemy.physical_attack * enemy.crit_mult + playerPhysicalDefense
                    enemy.stamina -= enemy.physical_attack
                else:
                    rpg.player.hp -= enemy.physical_attack + playerPhysicalDefense
                    enemy.stamina -= enemy.physical_attack
            else:
                enemy.hp -= ((enemy.maxhp * random.randrange(5, 10))/100)



def defend(rpg, enemy, who):
    if who == "Player":
        if rpg.player.stamina >= 0:
            if rpg.player.stamina - (rpg.player.speed - rpg.player.weapon.speed - rpg.player.armor.speed) != -1:
                rpg.combatGUI.increaseDefend = True
                rpg.player.stamina -= (rpg.player.speed - rpg.player.weapon.speed - rpg.player.armor.speed)
                if random.randrange(0, 100) <= rpg.player.luck:
                    enemy.hp -= (rpg.player.speed - rpg.player.weapon.speed - rpg.player.armor.speed)
        else: 
            rpg.combatGUI.increaseDefend = False
            rpg.player.hp -= (rpg.player.speed - rpg.player.weapon.speed - rpg.player.armor.speed)
            if random.randrange(0, 100) <= rpg.player.luck:
                if random.randrange(0, 100) <= rpg.player.crit_chance:
                    rpg.player.hp -= enemy.physical_attack * enemy.crit_mult
                else: 
                    rpg.player.hp -= enemy.physical_attack
    if who == "Monster":
        if enemy.stamina >= 0:
            if enemy.stamina - enemy.speed != -1:
                rpg.combatGUI.increaseDefend = True
                enemy.stamina - enemy.speed 
                if random.randrange(0, 100) <= enemy.luck:
                    rpg.player.hp -= enemy.speed 
        else:
            rpg.combatGUI.increaseDefend = False
            enemy.hp -= enemy.speed
            if random.randrange(0, 100) <= enemy.luck:
                if random.randrange(0, 100) <= enemy.crit_chance:
                    enemy.hp -= rpg.player.physical_attack * rpg.player.crit_mult
                else: 
                    enemy.hp -= rpg.player.physical_attack


def rest(rpg, enemy, who):
    if who == "Player":
        Resthp = ((rpg.player.maxhp * random.randrange(10, 25))/100)
        Reststamina = ((rpg.player.stamina_max * random.randrange(10, 25))/100)
        if rpg.player.hp + Resthp > rpg.player.maxhp:
            rpg.player.hp = rpg.player.maxhp
        else:
            rpg.player.hp += Resthp
        if rpg.player.stamina + Reststamina > rpg.player.stamina_max:
            rpg.player.stamina = rpg.player.stamina_max
        else:
            rpg.player.stamina += Reststamina

    if who == "Monster":
        Resthp = ((enemy.maxhp * random.randrange(10, 25))/100)
        Reststamina = ((enemy.stamina_max * random.randrange(10, 25))/100)
        if enemy.hp + Resthp > enemy.maxhp:
            enemy.hp = enemy.maxhp
        else:
            enemy.hp += Resthp
        if enemy.stamina + Reststamina > enemy.stamina_max:
            enemy.stamina = enemy.stamina_max
        else:
            enemy.stamina += Reststamina
       
def use(rpg):
    try:
        if(rpg.player.hp < rpg.player.maxhp * .75 and "Health Potion" in rpg.player.buffs):
            rpg.player.useBuff("Health Potion")
            message = "You now have",rpg.player.hp,"health left!"
            rpg.playerConsole.showNextText(rpg, "You used a health potion!", message, )
        if(rpg.player.stam < rpg.player.stam * .60 and "Stamina Potion" in rpg.player.buffs):
            rpg.player.useBuff("Stamina Potion")
        if(rpg.player.mana < rpg.player.mana * .65 and "Mana Potion" in rpg.rpg.player.buffs):
            rpg.player.useBuff("Mana Potion")
        