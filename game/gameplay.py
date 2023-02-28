from dice import Dice


class Game:

    # maybe player class should have this variables
    roll_score = 0
    turn_score = 0
    total_score = 0

    def __init__(self):
        pass

    def start(self):
        """Start the game"""
        pass
    
    def stop(self):
        # player2
        pass
    
    def roll(self):
        self.roll_score = Dice.roll(self)

    def turn(self):
        if self.roll_score == 1:
            self.turn_score = 0
            self.stop()
        else:
            self.turn_score += self.roll_score
        
    def total(self):
        self.total_score += self.turn_score

    def cheat(self):
        max_point = 6
        self.turn_score += max_point
        
    
