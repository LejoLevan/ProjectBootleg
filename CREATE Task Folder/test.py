class statSheet():
    def __init__(self, rpg):
        self.hpStat = Button(rpg, "")
        self.hpStat.statDefault(rpg, -375, 0, "HP", rpg.player.hp)
        self.stamStat = Button(rpg, "")
        self.stamStat.statDefault(rpg, -300, 0, "Stamina", rpg.player.stamina)
        self.manaStat = Button(rpg, "")
        self.manaStat.statDefault(rpg, -225, 0, "Mana", rpg.player.mana)
        self.speedStat = Button(rpg, "")
        self.speedStat.statDefault(rpg, -150, 0, "Speed", rpg.player.speed)
        self.physAtckStat = Button(rpg, "")
        self.physAtckStat.statDefault(rpg, -75, 0, "Physical Attack", rpg.player.physical_attack)
        self.magicAtckStat = Button(rpg, "")
        self.magicAtckStat.statDefault(rpg, 0, 0, "Magic Attack", rpg.player.magic_attack)
        self.physDefStat = Button(rpg, "")
        self.physDefStat.statDefault(rpg, -375, -200, "Physical Defense", rpg.player.physical_defense)
        self.magicDefStat = Button(rpg, "")
        self.magicDefStat.statDefault(rpg, -300, -200, "Magic Defense", rpg.player.magic_defense)
        self.fireResist = Button(rpg, "")
        self.fireResist.statDefault(rpg, -225, -200, "Fire Resistance", rpg.player.fire_resist)
        self.poisonResist = Button(rpg, "")
        self.poisonResist.statDefault(rpg, -150, -200, "Poison Resistance", rpg.player.poison_resist)
        self.accuracyStat = Button(rpg, "")
        self.accuracyStat.statDefault(rpg, -75, -200, "Accuracy", rpg.player.accuracy)
        self.critStat = Button(rpg, "")
        self.critStat.statDefault(rpg, 0, -200, "Crit Chance", rpg.player.crit_chance)
        self.critMult = Button(rpg, "")
        self.critMult.statDefault(rpg, -375, -400, "Crit Multiplier", rpg.player.crit_mult)
        self.luckStat = Button(rpg, "")
        self.luckStat.statDefault(rpg, -300, -400, "Luck", rpg.player.luck)
        self.hpStat.msg = "HP:", rpg.player.hp + "/"+ rpg.player.maxhp
        self.stamStat.msg = "Stamina:",rpg.player.stamina +"/"+ rpg.player.max_stamina
        self.manaStat.msg = "Mana:", rpg.player.mana + "/" + rpg.player.max_mana

    def showStats(self):
        self.hpStat.draw()
        self.stamStat.draw()
        self.manaStat.draw()
        self.speedStat.draw()
        self.physAtckStat.draw()
        self.magicAtckStat.draw()
        self.physDefStat.draw()
        self.magicDefStat.draw()
        self.fireResist.draw()
        self.poisonResist.draw()
        self.accuracyStat.draw()
        self.critStat.draw()
        self.critMult.draw()
        self.luckStat.draw()