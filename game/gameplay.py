from dice import Dice
from shell1 import Shell


class Game:

    def __init__(self):
        self.dice1 = Dice()
        self.player = Shell.current_player(self)
        self.roll_score = self.player.get_roll_score(self)
        self.turn_score = self.player.get_turn_score(self)
        self.total_score = self.player.get_total_score(self)

    def hold(self):
        self.total()
        print(f"Total score: {self.total_score}")
        self.turn_score = 0

    def roll(self):
        self.roll_score = self.dice1.roll()

    def turn(self):
        if self.roll_score == Dice.dice_min(self):
            self.turn_score = 0
        else:
            self.turn_score += self.roll_score

    def total(self):
        self.total_score += self.turn_score

    def cheat(self):
        self.turn_score += self.dice1.dice_max()
