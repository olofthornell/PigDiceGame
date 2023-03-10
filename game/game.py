"""Keep track of player score."""

from dice import Dice


class Game:
    """Game mechanics in Pig game."""

    def __init__(self):
        """Init the object."""
        self.dice1 = Dice()

    def roll(self, player):
        """Roll dice and get the score for the roll."""
        player.set_roll_score(self.dice1.roll())

    def hold(self, player):
        """Score for turn is transferred to total.

        Turn score is being set to 0.
        """
        self.total(player)
        player.set_turn_score(0)

    def turn(self, player):
        """Dice score is transferred to turn score. If dice score is 1.

        Then turn score is set to 0.
        """
        if player.get_roll_score() == 1:
            player.set_turn_score(0)
            self.total(player)
        else:
            turn = player.get_turn_score()
            roll = player.get_roll_score()
            new_turn_score = turn + roll
            player.set_turn_score(new_turn_score)

    def total(self, player):
        """Add the score of the turn to the total score."""
        new_total_score = player.get_total_score() + player.get_turn_score()
        player.set_total_score(new_total_score)

    def cheat(self, player):
        """Get max value on a roll with the dice."""
        player.set_roll_score(self.dice1.get_dice_max())
