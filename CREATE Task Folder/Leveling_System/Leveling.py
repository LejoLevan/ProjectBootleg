import pygame
from player import character
from Leveling_System import Classes

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
        