class blacksmith:
    def __init__(self, name):
        self.name = name
        self.misc_inventory = []
        self.forge = [] #items he can craft

    def craft(self, item, cost):
        if "copper" in rpg.player.misc_inventory:
            craftCopperSword = True
        else: 
            craftCopperSword = False

        if "" in rpg.player.misc_inventory:
            craft = True
        else: 
            craft = False


        if item in self.forge:
            if craftCopperSword == True:
                rpg.player.misc_inventory.append(item)
                rpg.player.gold -= cost

            if craft == True:
                rpg.player.misc_inventory.append(item)
                rpg.player.gold -= cost
