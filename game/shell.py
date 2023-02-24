import cmd
from gameplay import Game


class Shell(cmd.Cmd):

    def __init__(self):
        """Init the object."""
        super().__init__()
        self.game = Game()

    def do_start(self, _):
        self.game.start()
        print("Now let's roll the dice!")

    def do_cheat(self, _):
        print("Well look at that - you hit a six...")
        
    def do_turn_roll_score(self, _):
        print(f"You rolled a {self.game.rolled_dice()}.")
        print(f"You're score of the turn is {self.game.turn_roll_score()}")

    def do_exit(self, _):
        print("Well played! Bye")
        return True
