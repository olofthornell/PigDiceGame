import dice


class Game:

    turn_score = 0
    total_score = 0

    def __init__(self):
        pass

    def start(self):
        """Start the game"""
        pass
    
    def rolled_dice(self):
        dice1 = dice.Dice()
        dice_roll = dice1.roll()
        return dice_roll

    def turn_roll_score(self):
        if self.rolled_dice() == 1:
            self.turn_score = 0
            return self.turn_score
        else:
            self.turn_score += self.rolled_dice(self)
            return self.turn_score
    
    def cheat(self):
        max_point = 6
        self.turn_score += max_point
        
    
