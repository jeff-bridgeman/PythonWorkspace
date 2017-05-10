"""DOCSTRING."""


import random


class Spell:
    """Class Spell."""

    def __init__(self, name, cost, dmg, type):
        """Initisalize."""
        self.name = name
        self.cost = cost
        self.dmg = dmg
        self.type = type

    def generateDamage(self):
        """Function that generates Spell Damage."""
        low = self.dmg - 15
        high = self.dmg + 15
        return random.randrange(low, high)
