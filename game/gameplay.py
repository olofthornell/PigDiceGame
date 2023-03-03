from dice import Dice


class Game:

    def __init__(self, player):
        self.dice1 = Dice()
        self.roll_score = player.roll_score
        self.turn_score = player.turn_score
        self.total_score = player.total_score

    def roll(self):
        self.roll_score = self.dice1.roll()
        
    def hold(self):
        self.total()
        self.turn_score = 0

    def turn(self):
        if self.roll_score == 1:
            self.turn_score = 0
            self.total()
            print(f"Total: {self.total_score}")
        else:
            self.turn_score += self.roll_score

    def total(self):
        self.total_score += self.turn_score

    def cheat(self):
        self.turn_score += self.dice1.dice_max()
