"""The dice"""
import random


class Dice:
    """A class that holds information about a dice"""

    def __init__(self):
        self._dice_min = 1
        self._dice_max = 6

    def dice_min(self):
        return self._dice_min

    def dice_max(self):
        return self._dice_max

    def roll(self):
        return random.randint(1, 6)
