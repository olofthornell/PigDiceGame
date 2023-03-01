import cmd
from gameplay import Game
from player import Player
from shell2 import Shell2


class Shell(cmd.Cmd):

    def __init__(self):
        """Init game and player objects."""
        super().__init__()
        self.game1 = Game()
        self.human_player = Player(Shell2.player_name(self))
        self.computer_player = Player("cPIGu")
        self._current_player = self.human_player
        print("Lets go")
        
    def current_player(self):
        """Returning the current player"""
        return self._current_player
        
    def switch_player(self):
        if self._current_player == self.human_player:
            self._current_player = self.computer_player
        else:
            self._current_player = self.human_player
            
    def do_cheat(self, _):
        """Roll the dice and get a six"""
        self.game1.cheat()
        print("Well look at that - you have rolled a six...")
        print(f"You're score of the turn is {self.game1.turn_score}")
        
    def do_roll(self, _):
        self.game1.roll()
        self.game1.turn()
        print(f"You rolled a {self.game1.roll_score}.")
        print(f"You're score of the turn is {self.game1.turn_score}")
        
    def do_hold(self, _):
        self.game1.total()
        print(f"Total score: {self.game1.total_score}")
        # cPIGu

    def do_exit(self, _):
        print("Well played! Bye")
        return True
