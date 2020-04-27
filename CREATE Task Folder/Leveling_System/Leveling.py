import pygame
from main import player

player.Level = player.level
player.exp = 0
player.exp_cap = 50

def level(player.exp, player.level, player.exp_cap):
    print("Level:",player.level)
    print("Current Experience:",player.exp+"/"+player.exp_cap)
    print("Experience Until Next Level:",player.exp_cap-player.exp)
    
def NextLevel(player.exp, player.level, player.exp_cap):
    while (player.exp >= player.exp_cap):
        player.level = player.level + 1
        player.exp = player.exp-player.exp_cap
        print("You are now level:", player.level)
        player.exp_cap += 100
        print("The new exp cap is now:", player.exp_cap)
    if (player.level == 20):
        player.level = 20
        print("You are now max level:")
        player.exp_cap = player.exp

    def upgradeStats(player):
        
            #hp stats
            self.maxhp + 10
            self.hp + 10

            #attack stats
            self.physical_attack + 10
            self.magic_attack + 10

            #consume stats
            self.stamina + 10
            self.mana + 10

            #defense stats
            self.physical_defense + 10
            self.magic_defense + 10

            #resistance stats
            self.fire_resist + 5
            self.posion_resist + 5