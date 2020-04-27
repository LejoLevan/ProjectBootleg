class npc:
    def __init__(self, name, occupation):
        self.name = name
        self.occupation = occupation


#Add crit when we find out stuff
class ally:
    def __init__(self, name, hp, maxhp, physical_attack, magic_attack, stamina, mana, physical_defense, magic_defense, fire_resist, poison_resist, level, exp, exp_cap)
    #hp stats
        self.name = name
        self.maxhp = maxhp
        self.hp = hp

        #attack stats
        self.physical_attack = physical_attack
        self.magic_attack = magic_attack

        #consume stats
        self.stamina = stamina
        self.mana = mana

        #defense stats
        self.physical_defense = physical_defense
        self.magic_defense = magic_defense

        #resistance stats
        self.fire_resist = fire_resist
        self.posion_resist = poison_resist

        #level stats
        self.level = level
        self.exp = exp
        self.exp_cap = exp_cap