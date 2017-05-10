"""Import."""
import random
# import pprint
# from classes.magic import Spell


class Character:
    """Create Character class."""

    def __init__(self, hp, mp, atk, df, magic, items):
        """Initisalize."""
        self.maxhp = hp
        self.hp = hp
        self.maxmp = mp
        self.mp = mp
        self.atkl = atk - 10
        self.atkh = atk + 10
        self.df = df
        self.magic = magic
        self.items = items
        self.actions = ["Attack", "Magic", "Items"]

    def getMp(self):
        """Return Magic power on Character."""
        return self.mp

    def getMaxMp(self):
        """Return Max Magic power on Character."""
        return self.maxmp

    def getHp(self):
        """Return Health points on Character."""
        return self.hp

    def getMaxHp(self):
        """Return Max Health points on Character."""
        return self.maxhp

    def getAtk(self):
        """Return Attack power (Low, High) on Character."""
        return (self.atkl, self.atkh)

    def generateDamage(self):
        """Return Damage dealt."""
        return random.randrange(self.atkl, self.atkh)

    def takeDamage(self, dmg):
        """Damage check."""
        self.hp -= dmg
        if self.hp < 0:
            self.hp = 0
        return self.hp

    def reduceMp(self, cost):
        """Damage check."""
        self.mp -= cost
        if self.mp < 0:
            self.mp = 0
        return self.mp

    def heal(self, dmg):
        """Heal character."""
        self.hp += dmg
        if self.hp > self.maxhp:
            self.hp = self.maxhp

    def chooseAction(self):
        """Menu actions."""
        i = 1
        for item in self.actions:
            print("    " + str(i) + ".", item)
            i += 1

    def chooseMagic(self):
        """Choose magic spells."""
        i = 1

        for spell in self.magic:
            print("    " + str(i) + ".", spell.name, "(cost:",
                  str(spell.cost) + ")")
            i += 1

    def chooseItem(self):
        """Choose magic spells."""
        i = 1

        for items in self.items:
            print("    " + str(i) + ".", items["item"].name, ":",
                  items["item"].description + " (x" + str(items["quantity"])
                  + ")")
            i += 1
