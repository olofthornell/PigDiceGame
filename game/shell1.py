import cmd
from gameplay import Game


class Shell(cmd.Cmd):

    def __init__(self):
        """Init the object."""
        super().__init__()
        self.game1 = Game()
        print("Lets go")

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

    def do_exit(self, _):
        print("Well played! Bye")
        return True
