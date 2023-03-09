"""The dice"""
import random


class Dice:
    """A class that holds information about a dice"""

    def __init__(self):
        """Init the object."""
        self._dice_min = 1
        self._dice_max = 6

    def dice_min(self):
        """Min value of the dice"""
        return self._dice_min

    def dice_max(self):
        """Min value of the dice"""
        return self._dice_max

    def roll(self):
        "Get a value of the dice between 1 and 6"
        return random.randint(1, 6)
