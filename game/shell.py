import cmd
from gameplay import Game


class Shell(cmd.Cmd):

    def __init__(self):
        """Init the object."""
        super().__init__()
        self.game1 = Game()

    def do_start(self, _):
        print("Now let's roll the dice!")

    def do_cheat(self, _):
        """Roll the dice and get a six"""
        print("Well look at that - you hit a six...")
        
    def do_turn_score(self, _):
        self.game1.roll()
        self.game1.turn()
        print(f"You rolled a {self.game1.roll_score}.")
        print(f"You're score of the turn is {self.game1.turn_score}")

    def do_exit(self, _):
        print("Well played! Bye")
        return True
