from dice import Dice


class Game:

    def __init__(self):
        self.dice1 = Dice()
        # self._player = player

    def roll(self, player):
        """Rolles dice and get the score for the roll"""
        player.set_roll_score(self.dice1.roll())
        
    def hold(self, player):
        """Score for turn is transferred to total and turn score
        is being set to 0."""
        self.total(player)
        player.set_turn_score(0)

    def turn(self, player):
        """Dice score is transferred to turn score. If dice score is 1,
        then turn score is set to 0."""
        if player.get_roll_score() == 1:
            player.set_turn_score(0)
            self.total(player)
        else:
            turn = player.get_turn_score()
            roll = player.get_roll_score()
            new_turn_score = turn + roll
            player.set_turn_score(new_turn_score)

    def total(self, player):
        new_total_score = player.get_total_score() + player.get_turn_score()
        player.set_total_score(new_total_score)

    def cheat(self, player):
        player.set_roll_score(self.dice1.dice_max())
