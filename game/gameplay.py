from dice import Dice
from player import Player


class Game:

    # maybe player class should have this variables
    roll_score = 0
    turn_score = 0
    total_score = 0

    def __init__(self):
        self.players = [self.Player(), self.Player()]
        self.dice1 = Dice()

    def hold(self):
        self.total()
        print(f"Total score: {self.total_score}")
        self.turn_score = 0

    def roll(self):
        self.roll_score = self.dice1.roll()

    def turn(self):
        if self.roll_score == 1:
            self.turn_score = 0
        else:
            self.turn_score += self.roll_score

    def total(self):
        self.total_score += self.turn_score

    def cheat(self):
        self.turn_score += self.dice1.dice_max()
