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
    rpg.combatGUI.enemyHP.transparent = True
    rpg.combatGUI.enemyStamina.transparent = True
    rpg.combatGUI.enemyMana.transparent = True

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
    if rpg.player.hp > 0:
        rpg.playerConsole.showNextText(rpg, "It's now your turn", "Please a select an option", pygame.image.load("CREATE Task Folder\Image Assets\Battle_Images\Battle Icon.png"))
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
            use(rpg) 
            rpg.combatGUI.use = False

def checkHealths(rpg, enemy):
    if rpg.player.hp <= 0:
        rpg.combatGUI.battleOver = True
        rpg.playerConsole.showNextText(rpg, "How Unfortunate, You've Died", "Try again next time :(", pygame.image.load("CREATE Task Folder\Image Assets\Battle_Images\Battle Icon.png"))
        try:
            rpg.playerConsole.showNextText(rpg, "You have lost", "{} EXP".format(rpg.player.exp - (rpg.player.exp*.2)), pygame.image.load("CREATE Task Folder\Image Assets\Battle_Images\Battle Icon.png"))
            rpg.player.exp -= (rpg.player.exp*.2)
        except Exception:
            pass
        try:
            rpg.playerConsole.showNextText(rpg, "You have lost", "{} Gold".format(rpg.player.gold - (rpg.player.gold*.2)), pygame.image.load("CREATE Task Folder\Image Assets\Battle_Images\Battle Icon.png"))
            rpg.player.gold -= (rpg.player.gold * .2)
        except Exception:
            pass
        if random.randrange(0, 100) >= 85:
            inventory = random.choice(["Weapon Inventory", "Armor Inventory"])
            if inventory == "Weapon Inventory":
                rpg.playerConsole.showNextText(rpg, "You have lost", "{}".format(rpg.player.weapon.name), pygame.image.load("CREATE Task Folder\Image Assets\Battle_Images\Battle Icon.png"))
                item = rpg.player.weapon
            else:
                rpg.playerConsole.showNextText(rpg, "You have lost", "{}".format(rpg.player.armor.name), pygame.image.load("CREATE Task Folder\Image Assets\Battle_Images\Battle Icon.png"))
                item = rpg.player.armor
            rpg.player.deleteInventory(inventory, item)
        rpg.playerConsole.showNextText(rpg, "You now have", "{} HP".format(rpg.player.maxhp * .1), pygame.image.load("CREATE Task Folder\Image Assets\Battle_Images\Battle Icon.png"))
        rpg.player.hp = rpg.player.maxhp * .1
    if enemy.hp <= 0:
        rpg.combatGUI.battleOver = True
        loot(rpg, enemy)

def monsterTurn(rpg, enemy):
    if enemy.hp > 0:
        if enemy.intelligence == "Low":
            if random.randrange(0, 100) <= 85:
                attack(rpg, enemy, "Monster")
            else:
                if random.randrange(0, 100) <= 85:
                    defend(rpg, enemy, "Monster")
                else:
                    rest(rpg, enemy, "Monster")
        elif enemy.intelligence == "Medium":
            if enemy.hp <= enemy.hp *.25:
                if enemy.hp <= enemy.maxhp * .1:
                    rest(rpg, enemy, "Monster")
                else:
                    defend(rpg, enemy, "Monster")
            else:
                attack(rpg, enemy, "Monster")
        elif enemy.intelligence == "High":
            if enemy.hp > rpg.player.hp:
                if random.randrange(0, 100) <= 25:
                    defend(rpg, enemy, "Monster")
                    attack(rpg, enemy, "Monster")
            else:
                if enemy.hp <= enemy.hp * .5:
                    if enemy.hp <= enemy.maxhp * .3:
                        rest(rpg, enemy, "Monster")
                    elif random.randrange(0, 100) <= 10:
                        rest(rpg, enemy, "Monster")
                        defend(rpg, enemy, "Monster")
                    else:
                        defend(rpg, enemy, "Monster")
                    if enemy.hp <= enemy.maxhp * .1:
                        rpg.combatGUI.battleOver = True
                else:
                    attack(rpg, enemy, "Monster")
    

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
        monsterPhysicalDefense = enemy.physical_defense
        monsterMagicDefense = enemy.magic_defense
        if rpg.combatGUI.increasePlayerDefend == True:
            monsterPhysicalDefense += round(enemy.physical_defense * 0.1)
            monsterMagicDefense += round(enemy.magic_defense * 0.1)

        if rpg.player.profession == "Apprentice" or rpg.player.profession == "Warlock" or rpg.player.profession == "Wizard":
            if rpg.player.mana >= rpg.player.magic_attack:
                if random.randrange(0, 100) <= rpg.player.accuracy:
                    if random.randrange(0, 100) <= rpg.player.crit_chance:
                        if ((rpg.player.magic_attack + rpg.player.weapon.magic_attack) * rpg.player.crit_mult) - monsterMagicDefense < 0:
                            rpg.playerConsole.showNextText(rpg, "You crit and dealt", "0 damage", pygame.image.load("CREATE Task Folder\Image Assets\Battle_Images\Battle Icon.png"))
                        else:
                            rpg.playerConsole.showNextText(rpg, "You crit and dealt", "{} damage".format(((rpg.player.magic_attack + rpg.player.weapon.magic_attack) * rpg.player.crit_mult) - monsterMagicDefense), pygame.image.load("CREATE Task Folder\Image Assets\Battle_Images\Battle Icon.png"))
                            enemy.hp -= ((rpg.player.magic_attack + rpg.player.weapon.magic_attack) * rpg.player.crit_mult) - monsterMagicDefense
                        rpg.player.mana -= rpg.player.magic_attack
                        rpg.player.weapon.durability -= ((rpg.player.magic_attack + rpg.player.weapon.magic_attack) * rpg.player.crit_mult) - monsterMagicDefense
                    else:
                        if rpg.player.magic_attack + rpg.player.weapon.magic_attack - monsterMagicDefense < 0:
                            rpg.playerConsole.showNextText(rpg, "You dealt", "0 damage", pygame.image.load("CREATE Task Folder\Image Assets\Battle_Images\Battle Icon.png"))
                        else:
                            rpg.playerConsole.showNextText(rpg, "You dealt", "{} damage".format((rpg.player.magic_attack + rpg.player.weapon.magic_attack) - monsterMagicDefense), pygame.image.load("CREATE Task Folder\Image Assets\Battle_Images\Battle Icon.png"))
                            enemy.hp -= rpg.player.magic_attack + rpg.player.weapon.magic_attack - monsterMagicDefense
                        rpg.player.mana -= rpg.player.magic_attack
                        rpg.player.weapon.durability -= rpg.player.magic_attack + rpg.player.weapon.magic_attack - monsterMagicDefense
                else:
                    rpg.playerConsole.showNextText(rpg, "You", "missed", pygame.image.load("CREATE Task Folder\Image Assets\Battle_Images\Battle Icon.png"))
            else:
                damageTaken = (round((rpg.player.maxhp * random.randrange(5, 10))/100))
                rpg.playerConsole.showNextText(rpg, "You don't enough stamina", "You've taken {} damage :(".format(damageTaken), pygame.image.load("CREATE Task Folder\Image Assets\Battle_Images\Battle Icon.png"))
                rpg.player.hp -= damageTaken
        else:
            if rpg.player.stamina >= rpg.player.physical_attack:
                if random.randrange(0, 100) <= rpg.player.accuracy:
                    if random.randrange(0, 100) <= rpg.player.crit_chance:
                        if ((rpg.player.physical_attack + rpg.player.weapon.physical_attack) * rpg.player.crit_mult) - monsterPhysicalDefense <0:
                            rpg.playerConsole.showNextText(rpg, "You crit and dealt", "0 damage", pygame.image.load("CREATE Task Folder\Image Assets\Battle_Images\Battle Icon.png"))
                        else:
                            rpg.playerConsole.showNextText(rpg, "You crit and dealt", "{} damage".format(((rpg.player.physical_attack + rpg.player.weapon.physical_attack) * rpg.player.crit_mult) - monsterPhysicalDefense), pygame.image.load("CREATE Task Folder\Image Assets\Battle_Images\Battle Icon.png"))
                            enemy.hp -= ((rpg.player.physical_attack + rpg.player.weapon.physical_attack) * rpg.player.crit_mult) - monsterPhysicalDefense
                        rpg.player.stamina -= rpg.player.physical_attack
                        rpg.player.weapon.durability -= ((rpg.player.physical_attack + rpg.player.weapon.physical_attack) * rpg.player.crit_mult) - monsterPhysicalDefense
                    else:
                        if rpg.player.physical_attack + rpg.player.weapon.physical_attack - monsterPhysicalDefense < 0:
                            rpg.playerConsole.showNextText(rpg, "You dealt", "0 damage", pygame.image.load("CREATE Task Folder\Image Assets\Battle_Images\Battle Icon.png"))
                        else:
                            rpg.playerConsole.showNextText(rpg, "You dealt", "{} damage".format(rpg.player.physical_attack + rpg.player.weapon.physical_attack - monsterPhysicalDefense), pygame.image.load("CREATE Task Folder\Image Assets\Battle_Images\Battle Icon.png"))
                            enemy.hp -= rpg.player.physical_attack + rpg.player.weapon.physical_attack - monsterPhysicalDefense
                        rpg.player.stamina -= rpg.player.physical_attack
                        rpg.player.weapon.durability -= rpg.player.physical_attack + rpg.player.weapon.physical_attack - monsterPhysicalDefense
                else:
                    rpg.playerConsole.showNextText(rpg, "You", "missed", pygame.image.load("CREATE Task Folder\Image Assets\Battle_Images\Battle Icon.png"))
            else:
                damageTaken = (round((rpg.player.maxhp * random.randrange(5, 10))/100))
                rpg.playerConsole.showNextText(rpg, "You don't enough stamina", "You've taken {} damage :(".format(damageTaken), pygame.image.load("CREATE Task Folder\Image Assets\Battle_Images\Battle Icon.png"))
                rpg.player.hp -= damageTaken

    if who == "Monster":
        playerPhysicalDefense = rpg.player.physical_defense
        playerMagicDefense = rpg.player.magic_defense
        if rpg.combatGUI.increasePlayerDefend == True:
            playerPhysicalDefense += round(rpg.player.physical_defense * 0.1)
            playerMagicDefense += round(rpg.player.magic_defense * 0.1)
            
        if enemy.profession == "Mage":
            if enemy.mana >= enemy.magic_attack:
                if random.randrange(0, 100) <= enemy.accuracy:
                    if random.randrange(0, 100) <= enemy.crit_chance:
                        if (enemy.magic_attack * enemy.crit_mult) - playerMagicDefense < 0:
                            rpg.playerConsole.showNextText(rpg, "{} has crit and dealt".format(enemy.name), "0 damage", pygame.image.load(enemy.icon))
                        else:
                            rpg.player.hp -= (enemy.magic_attack * enemy.crit_mult) - playerMagicDefense
                            rpg.playerConsole.showNextText(rpg, "{} has crit and dealt".format(enemy.name), "{} damage".format(enemy.magic_attack * enemy.crit_mult - playerMagicDefense), pygame.image.load(enemy.icon))
                        enemy.mana -= enemy.magic_attack
                        rpg.player.armor.durability -= enemy.magic_attack * enemy.crit_mult
                    else:
                        if enemy.magic_attack - playerMagicDefense < 0:
                            rpg.playerConsole.showNextText(rpg, "{} has crit and dealt".format(enemy.name), "0 damage", pygame.image.load(enemy.icon))
                        else:
                            rpg.playerConsole.showNextText(rpg, "{} has crit and dealt".format(enemy.name), "{} damage".format(enemy.magic_attack * enemy.crit_mult - playerMagicDefense), pygame.image.load(enemy.icon))
                            rpg.player.hp -= enemy.magic_attack - playerMagicDefense
                        enemy.mana -= enemy.magic_attack
                        rpg.player.armor.durability -= enemy.magic_attack
                else:
                    rpg.playerConsole.showNextText(rpg, "{}".format(enemy.name), "missed", pygame.image.load(enemy.icon))
            else:
                damageTaken = (round((enemy.maxhp * random.randrange(5, 10))/100))
                rpg.playerConsole.showNextText(rpg, "{} didn't have enough stamina".format(enemy.name), "{} has taken {} damage :(".format(enemy.name, damageTaken), pygame.image.load(enemy.icon))
                enemy.hp -= damageTaken
        else:
            if enemy.stamina >= enemy.physical_attack:
                if random.randrange(0, 100) <= enemy.accuracy:
                    if random.randrange(0, 100) <= enemy.crit_chance:
                        if (enemy.physical_attack * enemy.crit_mult) - playerPhysicalDefense < 0:
                            rpg.playerConsole.showNextText(rpg, "{} has crit and dealt".format(enemy.name), "0 damage", pygame.image.load(enemy.icon))
                        else:
                            rpg.playerConsole.showNextText(rpg, "{} has crit and dealt".format(enemy.name), "{} damage".format(enemy.physical_attack * enemy.crit_mult - playerPhysicalDefense), pygame.image.load(enemy.icon))
                            rpg.player.hp -= (enemy.physical_attack * enemy.crit_mult) - playerPhysicalDefense
                        enemy.stamina -= enemy.physical_attack
                        rpg.player.armor.durability -= (enemy.physical_attack * enemy.crit_mult)
                    else:
                        if enemy.physical_attack - playerPhysicalDefense < 0:
                            rpg.playerConsole.showNextText(rpg, "{} dealt".format(enemy.name), "0 damage", pygame.image.load(enemy.icon))
                        else:
                            rpg.playerConsole.showNextText(rpg, "{} dealt".format(enemy.name), "{} damage".format(enemy.physical_attack), pygame.image.load(enemy.icon))
                            rpg.player.hp -= enemy.physical_attack - playerPhysicalDefense
                        enemy.stamina -= enemy.physical_attack
                        rpg.player.armor.durability -= enemy.physical_attack
                else:
                    rpg.playerConsole.showNextText(rpg, "{}".format(enemy.name), "missed", pygame.image.load(enemy.icon))
            else:
                damageTaken = (round((enemy.maxhp * random.randrange(5, 10))/100))
                rpg.playerConsole.showNextText(rpg, "{} didn't have enough stamina".format(enemy.name), "{} has taken {} damage :(".format(enemy.name, damageTaken), pygame.image.load(enemy.icon))
                enemy.hp -= damageTaken

def defend(rpg, enemy, who):
    if who == "Player":
        if rpg.player.stamina >= 0:
            if rpg.player.stamina - (rpg.player.speed - rpg.player.weapon.speed - rpg.player.armor.speed) != -1:
                rpg.combatGUI.increasePlayerDefend = True
                rpg.playerConsole.showNextText(rpg, "You have", "Successfully Defended", pygame.image.load("CREATE Task Folder\Image Assets\Battle_Images\Battle Icon.png"))
                rpg.player.stamina -= (rpg.player.speed - rpg.player.weapon.speed - rpg.player.armor.speed)
                if random.randrange(0, 100) <= rpg.player.luck:
                    enemy.hp -= (rpg.player.speed - rpg.player.weapon.speed - rpg.player.armor.speed)
        else: 
            rpg.combatGUI.increasePlayerDefend = False
            rpg.playerConsole.showNextText(rpg, "You have", "Failed to Defend", pygame.image.load("CREATE Task Folder\Image Assets\Battle_Images\Battle Icon.png"))
            rpg.player.hp -= (rpg.player.speed - rpg.player.weapon.speed - rpg.player.armor.speed)
            if random.randrange(0, 100) <= rpg.player.luck:
                if random.randrange(0, 100) <= rpg.player.crit_chance:
                    rpg.player.hp -= enemy.physical_attack * enemy.crit_mult
                else: 
                    rpg.player.hp -= enemy.physical_attack
                    rpg.playerConsole.showNextText(rpg, "You have", "Loss Health", pygame.image.load("CREATE Task Folder\Image Assets\Battle_Images\Battle Icon.png"))

    if who == "Monster":
        if enemy.stamina >= 0:
            if enemy.stamina - enemy.speed != -1:
                rpg.combatGUI.increaseMonsterDefend = True
                rpg.playerConsole.showNextText(rpg, "{} has".format(enemy.name), "Successfully Defended", pygame.image.load(enemy.icon))
                enemy.stamina - enemy.speed 
                if random.randrange(0, 100) <= enemy.luck:
                    rpg.player.hp -= enemy.speed 
        else:
            rpg.combatGUI.increaseMonsterDefend = False
            rpg.playerConsole.showNextText(rpg, "{} has".format(enemy.name), "Failed to Defend", pygame.image.load(enemy.icon))
            enemy.hp -= enemy.speed
            if random.randrange(0, 100) <= enemy.luck:
                if random.randrange(0, 100) <= enemy.crit_chance:
                    enemy.hp -= rpg.player.physical_attack * rpg.player.crit_mult
                else: 
                    enemy.hp -= rpg.player.physical_attack
                    rpg.playerConsole.showNextText(rpg, "{} has".format(enemy.name), "Taken Damage", pygame.image.load(enemy.icon))


def rest(rpg, enemy, who):
    if who == "Player":
        Resthp = (round((rpg.player.maxhp * random.randrange(10, 25))/100))
        Reststamina = (round((rpg.player.stamina_max * random.randrange(10, 25))/100))
        if rpg.player.hp + Resthp > rpg.player.maxhp:
            rpg.playerConsole.showNextText(rpg, "You have gained", "Max health", pygame.image.load("CREATE Task Folder\Image Assets\Battle_Images\Battle Icon.png"))
            rpg.player.hp = rpg.player.maxhp
        else:
            rpg.playerConsole.showNextText(rpg, "You have gained", "{} HP".format(Resthp), pygame.image.load("CREATE Task Folder\Image Assets\Battle_Images\Battle Icon.png"))
            rpg.player.hp += Resthp
        if rpg.player.stamina + Reststamina > rpg.player.stamina_max:
            rpg.playerConsole.showNextText(rpg, "You have gained", "Max Stamina", pygame.image.load("CREATE Task Folder\Image Assets\Battle_Images\Battle Icon.png"))
            rpg.player.stamina = rpg.player.stamina_max
        else:
            rpg.playerConsole.showNextText(rpg, "You have gained", "{} Stamina", pygame.image.load("CREATE Task Folder\Image Assets\Battle_Images\Battle Icon.png"))
            rpg.player.stamina += Reststamina

    if who == "Monster":
        Resthp = (round((enemy.maxhp * random.randrange(10, 25))/100))
        Reststamina = (round((enemy.stamina_max * random.randrange(10, 25))/100))
        if enemy.hp + Resthp > enemy.maxhp:
            rpg.playerConsole.showNextText(rpg, "{} has gained".format(enemy.name), "Max health", pygame.image.load(enemy.icon))
            enemy.hp = enemy.maxhp
        else:
            rpg.playerConsole.showNextText(rpg, "{} has gained".format(enemy.name), "{} HP".format(Resthp), pygame.image.load(enemy.icon))
            enemy.hp += Resthp
        if enemy.stamina + Reststamina > enemy.stamina_max:
            rpg.playerConsole.showNextText(rpg, "{} has gained".format(enemy.name), "Max Stamina", pygame.image.load(enemy.icon))
            enemy.stamina = enemy.stamina_max
        else:
            rpg.playerConsole.showNextText(rpg, "{} has gained".format(enemy.name), "{} Stamina".format(Reststamina), pygame.image.load(enemy.icon))
            enemy.stamina += Reststamina
       
def use(rpg):
    try:
        if(rpg.player.hp < rpg.player.maxhp * .75 and "Health Potion" in rpg.player.buffs):
            rpg.player.useBuff("Health Potion")
            battleMessage = "You now have",rpg.player.hp,"health left!"
            rpg.playerConsole.showNextText(rpg, "You used a health potion!", battleMessage, pygame.image.load("CREATE Task Folder\Image Assets\Battle_Images\Battle Icon.png"))
        if(rpg.player.stamina < rpg.player.stamina_max * .60 and "Stamina Potion" in rpg.player.buffs):
            rpg.player.useBuff("Stamina Potion")
            battleMessage = "You now have", rpg.player.stamina, "stamina left!"
            rpg.playerConsole.showNextText(rpg, "You used a Stamina Potion!", battleMessage, pygame.image.load("CREATE Task Folder\Image Assets\Battle_Images\Battle Icon.png"))
        if(rpg.player.mana < rpg.player.mana_max * .65 and "Mana Potion" in rpg.rpg.player.buffs):
            rpg.player.useBuff("Mana Potion")
            battleMessage = "You now have", rpg.player.mana, "mana left!"
            rpg.playerConsole.showNextText(rpg, "You used a mana potion!", battleMessage, pygame.image.load("CREATE Task Folder\Image Assets\Battle_Images\Battle Icon.png"))
        elif(rpg.player.hp > rpg.player.maxhp * .75 and rpg.player.stamina > rpg.player.stamina_max * .60 and rpg.player.mana > rpg.player.mana_max * .65):
            rpg.playerConsole.showNextText(rpg, "You do not need to use a potion right now!", " ", pygame.image.load("CREATE Task Folder\Image Assets\Battle_Images\Battle Icon.png"))
        elif("Health Potion" not in rpg.player.buffs or "Stamina Potion" not in rpg.player.buffs or "Mana Potion" not in rpg.player.buffs):
            if(rpg.player.hp < rpg.player.maxhp * .75 and "Health Potion" not in rpg.player.buffs):
                rpg.playerConsole.showNextText(rpg, "You do not have a health potion!", " ", pygame.image.load("CREATE Task Folder\Image Assets\Battle_Images\Battle Icon.png"))
            if(rpg.player.stamina < rpg.player.stamina_max * .60 and "Stamina Potion" not in rpg.player.buffs):
                rpg.playerConsole.showNextText(rpg, "You do not have a stamina potion!", " ", pygame.image.load("CREATE Task Folder\Image Assets\Battle_Images\Battle Icon.png"))
            if(rpg.player.mana < rpg.player.mana_max * .65 and "Mana Potion" not in rpg.player.buffs):
                rpg.playerConsole.showNextText(rpg, "You do not have a mana potion!", " ", pygame.image.load("CREATE Task Folder\Image Assets\Battle_Images\Battle Icon.png"))
    except:
        pass