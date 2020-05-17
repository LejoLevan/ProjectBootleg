
class blacksmith:
    def __init__(self, name):
        self.name = name
        self.inventory = []
        self.forge = ["Copper Sword", "Copper Shiv", "Copper Armor"]

    def craft(self, rpg, item, cost):
        if "copper" and "copper" and "copper" and "copper" and "leather" and "leather" and "string" and "string" and "string" in rpg.player.miscs:
            craftCopperSword = True
        else: 
            craftCopperSword = False

        if "copper" and "leather" and "string" and "string" in rpg.player.miscs:
            craftCopperShiv = True
        else: 
            craftCopperShiv = False

        if "copper" and "copper" and "copper" and "copper" and "leather" and "leather" and "leather" in rpg.player.miscs:
            craftCopperArmor = True
        else: 
            craftCopperArmor = False

        if item in self.forge:
            if craftCopperSword == True:
                rpg.player.miscs.append(item)
                rpg.player.gold -= cost
                craftCopperSword = False
                rpg.player.miscs.remove("copper", "copper", "copper", "copper", "leather", "leather", "string", "string", "string")

            if craftCopperShiv == True:
                rpg.player.miscs.append(item)
                rpg.player.gold -= cost
                craftCopperShiv = False
                rpg.player.miscs.remove("copper", "leather", "string", "string")

            if craftCopperArmor == True:
                rpg.player.miscs.append(item)
                rpg.player.gold -= cost
                craftCopperArmor = False
                rpg.player.miscs.remove("copper", "copper", "copper", "copper", "leather", "leather", "leather")
