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

        def do_exit(self, _):
            print("Well played! Bye")
            return True
