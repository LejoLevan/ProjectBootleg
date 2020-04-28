import pygame
from main import player
from player import character
from Leveling import level
from Leveling import NextLevel

player = character()


class Classes:
    def __init__(self, name, money):
        self.name = name

def Squire():
    if(player.profession == "Squire" and player.level == 0):
        squire = Classes("Squire")
    if (player.level == 3):
        squire = Classes("Knight")
    if (player.level == 10):
        squire = Classes("Templar")
    if (player.level == 20):
        squire = Classes("Holy Paladin")

def Thief():
    if(player.profession == "Thief" and player.level == 0):
        Thief = Classes("Thief")
    if (player.level == 3):
        Thief = Classes("Scoundrel")
    if (player.level == 10):
        Thief = Classes("Rogue")
    if (player.level == 20):
        Thief = Classes("Assassin")

def apprentice():
    if(player.profession == "Apprentice" and player.level == 0):
        apprentice = Classes("Apprentice")
    if(player.level==3):
        apprentice = Classes("Warlock")
    if(player.level==10):
        apprentice = Classes("Wizard")
    if(player.level==20):
        apprentice = Classes("Head Mage")
    
def Commoner(): 
    Commoner = Classes("Commoner")
    if (player.level == 3):
        Commoner = Classes("noble")
    if(player.level==10):
        apprentice = Classes("Military leader")
    if(player.level==20):
        apprentice = Classes("Shroud")
        accuracy = 10000000000000

def warrior():
    if(player.profession == "Warrior" and player.level == 0):
        warrior = Classes("Warrior")
    if(player.level == 3):
        warrior = Classes("Berserker")
    if(player.level == 10):
        warrior = Classes("Gladiator")
    if(player.level == 20):
        warrior = Classes("Slayer")

def archer():
    if(player.profession == "Archer" and player.level == 0):
        archer = Classes("Archer")
    if(player.level == 3):
        archer = Classes("Hunter")
    if(player.level == 10):
        archer = Classes("Marksman")
    if(player.level == 20):
        archer = Classes("Ranger")