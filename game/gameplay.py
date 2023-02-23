import dice


class Game:

    turn_score = 0
    total_score = 0

    def __init__(self):
        pass

    def start(self):
        """Start the game"""
        pass

    def roll_dice(self):
        dice_roll = dice.Dice.roll(self)
        if dice_roll == 1:
            self.turn_score = 0
        else:
            self.turn_score += dice_roll
        
    
