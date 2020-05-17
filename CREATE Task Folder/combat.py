import random
import pygame

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
    while battleOver == False:
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

def whoFirst(rpg, enemy):
    pass

def playerTurn(rpg, enemy):
    pass

def checkHealths(rpg, enemy):
    pass

def monsterTurn(rpg, enemy):
    pass
