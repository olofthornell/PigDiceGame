from dice import Dice


class Game:

    # maybe player class should have this variables
    roll_score = 0
    turn_score = 0
    total_score = 0

    def __init__(self):
        self.dice1 = Dice

    def hold(self):
        # player2
        pass

    def roll(self):
        self.roll_score = self.dice1.roll(self)

    def turn(self):
        if self.roll_score == 1:
            self.turn_score = 0
        else:
            self.turn_score += self.roll_score

    def total(self):
        self.total_score += self.turn_score

    def cheat(self):
        self.turn_score += self.dice1.
        
    
