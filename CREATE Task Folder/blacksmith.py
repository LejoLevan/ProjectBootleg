class blacksmith:
    def __init__(self, name):
        self.name = name
        self.inventory = []
        self.forge = ["Copper Sword","Copper Shiv"] #items he can craft

    def craft(self, item, cost):
        if "copper","copper","copper","copper","leather","leather","string","string","string" in rpg.player.miscs:
            craftCopperSword = True
        else: 
            craftCopperSword = False

        if "copper","leather","string","string" in rpg.player.miscs:
            craftCopperShiv = True
        else: 
            craftCopperShiv = False


        if item in self.forge:
            if craftCopperSword == True:
                rpg.player.miscs.append(item)
                rpg.player.gold -= cost
                craftCopperSword = False
                rpg.player.miscs.remove("copper","copper","copper","copper","leather","leather","string","string","string")

            if craftCopperShiv == True:
                rpg.player.miscs.append(item)
                rpg.player.gold -= cost
                craftCopperShiv = False
                rpg.player.miscs.remove("copper","leather","string","string")
