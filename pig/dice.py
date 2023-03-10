"""The dice."""
import random


class Dice():
    """A class that holds information about a dice."""

    def __init__(self):
        """Init the object."""
        self.dice_min = 1
        self.dice_max = 6

    def get_dice_min(self):
        """Min value of the dice."""
        return self.dice_min

    def get_dice_max(self):
        """Min value of the dice."""
        return self.dice_max

    def roll(self):
        """Get a value of the dice between 1 and 6."""
        return random.randint(1, 6)
