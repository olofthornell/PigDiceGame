import cmd
import shell1


class Shell2(cmd.Cmd):

    def __init__(self):
        """Init the object."""
        super().__init__()
        self._player_name = input("Enter your name? ")
        self.print_menu()
        
    def print_menu(self):
        print()
        print()
        print(f"Welcome {self._player_name}! Let's pass some pigs")
        print()
        print("Commands:")
        print("-" * 79)
        print(f"{'start':20}| Start a new round of the game ")
        print("-" * 79)
        print(f"{'rules':20}| Read the rules of the game")
        print("-" * 79)
        print(f"{'difficulty coward':20}| Opponent cPIGu is a coward")
        print("-" * 79)
        print(f"{'difficulty moderate':20}| Opponent cPIGu is moderate")
        print("-" * 79)
        print(f"{'difficulty bold':20}| Opponent cPIGu is bold")
        print("-" * 79)
        print(f"{'high_score':20}| Show list of players wins")
        print("-" * 79)
        print(f"{'exit':20}| Exit the program")
        print("-" * 79)

    def player_name(self):
        return self._player_name

    def do_difficulty(self, arg):
        """Choose personality on opponent cPIGu"""
        return arg

    def do_start(self, _):
        """Start the game"""
        shell1.Shell(self._player_name).cmdloop()

    def do_rules(self, _):
        "Rules for pig game"
        print()
        print("-" * 79)
        print("Pig game rules:")
        print("-" * 79)
        print("1. Roll the dice and try to be the first to reach 100 points.")
        print("2. Players take turns and roll as many times as they wish.")
        print("3. All roll results are added to a running total.")
        print("4. If you roll a 1 you loose all gained score for the turn.")
        print("5. Ending a turn will save your points to a total.")
        print()
        
    def do_high_score(self, _):
        """Show high score"""
        pass

    def do_exit(self, _):
        """Exit the program"""
        print("Exit the program")
        print("See you next time")
        return True
    
    def default(self, line):
        print("Wrong command. Type 'help' for a list of commands.")
