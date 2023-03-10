"""Cmdloop that holds the gameplay."""

import cmd
from pig.gameplay import Gameplay


class Shell1(cmd.Cmd):
    """Command actions for dice game main menu."""

    def __init__(self, player):
        """Init gameplay object."""
        super().__init__()
        self.gameplay = Gameplay(player)

    def do_difficulty(self, arg):
        """Choose personality on opponent cPIGu."""
        self.gameplay.set_difficulty(arg)

    def do_cheat(self, _):
        """Roll the dice and get a six."""
        self.gameplay.cheat()

    def do_roll(self, _):
        """Roll the dice."""
        self.gameplay.roll()

    def do_hold(self, _):
        """End turn and collect points."""
        self.gameplay.hold()

    def do_exit(self, _):
        """Exit gameplay and return to main menu."""
        print("Returning to main menu.")
        return True

    def postloop(self):
        """Show help information after the gameplay ends."""
        print("Type 'help' for a list of commands.")
        super().postloop
