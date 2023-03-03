from dice import Dice


class Game:

    def __init__(self):
        self.dice1 = Dice()
        # self._player = player

    def roll(self, player):
        player.set_roll_score(self.dice1.roll())
        
    def hold(self, player):
        self.total(player)
        player.set_turn_score(0)

    def turn(self, player):
        if player.get_roll_score() == 1:
            player.set_turn_score(0)
            self.total(player)
            print(f"Total: {player.get_total_score()}")
        else:
            turn = player.get_turn_score()
            roll = player.get_roll_score()
            new_turn_score = turn + roll
            player.set_turn_score(new_turn_score)

    def total(self, player):
        new_total_score = player.get_total_score() + player.get_turn_score()
        player.set_total_score(new_total_score)

    def cheat(self, player):
        player.set_roll_score(6) #self.dice1.dice_max
