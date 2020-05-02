class blacksmith:
    def __init__(self, name):
        self.name = name
        self.inventory = []
        self.forge = [] #items he can craft

    def craft(self, item, cost):
        if "" in rpg.player.inventory:
            craftSword = True
        else: 
            craftSword = False

        if "" in rpg.player.inventory:
            craft = True
        else: 
            craft = False


        if item in self.forge:
            if craftSword == True:
                rpg.player.inventory.append(item)
                rpg.player.gold -= cost

            if craft == True:
                rpg.player.inventory.append(item)
                rpg.player.gold -= cost
