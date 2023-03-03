import cmd
from gameplay import Game
from player import Player


class Shell(cmd.Cmd):

    def __init__(self, player_name):
        """Init game and player objects."""
        super().__init__()
        self.human_player = Player(player_name)
        self.computer_player = Player("cPIGu")
        self._current_player = self.human_player
        self.game1 = Game(self._current_player)
        print("Lets go")
        
    def current_player(self):
        """Returning the current player"""
        return self._current_player
        
    def switch_player(self):
        """Switch between human player and cpu"""
        if self._current_player == self.human_player:
            self._current_player = self.computer_player
            # cPIGu playes
        else:
            self._current_player = self.human_player
            
    def do_cheat(self, _):
        """Roll the dice and get a six"""
        self.game1.cheat()
        print("Well look at that - you rolled a six...")
        print(f"You're score of the turn is {self.game1.turn_score}")
        
    def do_roll(self, _):
        print(f"{self.current_player().get_name()}")
        self.game1.roll()
        self.game1.turn()
        print(f"You rolled a {self.game1.roll_score}.")
        print(f"You're score of the turn is {self.game1.turn_score}")
        if self.game1.roll_score == 1:
            self.switch_player()
        
    def do_hold(self, _):
        self.game1.hold()
        print(f"Total score: {self.game1.total_score}")
        self.switch_player()
        # cPIGu

    def do_exit(self, _):
        print("Well played! Bye")
        return True
