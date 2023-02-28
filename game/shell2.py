import cmd
import shell1


class Shell2(cmd.Cmd):

    def __init__(self):
        """Init the object."""
        super().__init__()
        print("Print 'settings' for setting, print 'start_game' to start")

    def do_settings(self, _):
        print("Change stuff")

    def do_start_game(self, _):
        shell1.Shell().cmdloop()

    def do_exit(self, _):
        print("Well played! Bye")
        return True
