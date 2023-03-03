import cmd
import shell1
from player import Player


class Shell2(cmd.Cmd):

    def __init__(self):
        """Init the object."""
        super().__init__()
        self._player_name = input("What is your name? ")
        print()
        print(f"Welcome {self._player_name}! Let's pass some pigs")
        print("-" * 43)
        print("Commands:")
        print("* 'difficulty' + 'C' (coward), 'N' (normal) or 'B' (bold)")
        print("* 'start_game' to start")

    def player_name(self):
        return self._player_name

    def do_difficulty(self, arg):
        """Choose personality on opponent cPIGu"""
        return arg

    def do_start_game(self, _):
        shell1.Shell(self._player_name).cmdloop()

    def do_exit(self, _):
        print("Well played! Bye")
        return True
