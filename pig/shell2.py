"""Cmdloop that creates a outer shell and workes as a main menu."""

import time
import cmd
import shell1
from pig.high_score import HighScore
from pig.player import Player


class Shell2(cmd.Cmd):
    """Command actions for dice game gameplay."""

    def __init__(self):
        """Init the object."""
        super().__init__()
        self.print_welcome_graphic()
        self._player_name = input("Enter your name? ").lower()
        self.player = Player(self._player_name)
        self.h_score = HighScore()
        if self._player_name in self.h_score.high_score_dict:
            self.h_score.move_player_info(self.player, self._player_name)
        self.print_menu()

    def print_welcome_graphic(self):
        """Print art for pig game."""
        print('\n' * 40)
        print('            88            ')
        print()
        print('8b,dPPYba,  88  ,adPPYb,d8')
        print('88P"    "8a 88 a8"    "Y88')
        print('88       d8 88 8b       88')
        print('88b,   ,a8" 88 "8a,   ,d88 ')
        print('88`YbbdP""  88  ""YbbdP"Y8')
        print('88              aa,    ,88 ')
        print('88               "Y8bbdP"')
        print('')

    def print_menu(self):
        """Print main menu."""
        print()
        print()
        print(f"Welcome {self._player_name}! Let's pass some pigs")
        time.sleep(2)
        print()
        print("Commands:")
        print("-" * 79)
        print(f"{'start':20}| Start a new round of the game ")
        print("-" * 79)
        print(f"{'rules':20}| Read the rules of the game")
        print("-" * 79)
        print(f"{'high_score':20}| Show list of players wins")
        print("-" * 79)
        print(f"{'clear_high_score':20}| Clear the high score")
        print("-" * 79)
        print(f"{'change_name':20}| Change your nickname")
        print("-" * 79)
        print(f"{'exit':20}| Exit the program")
        print("-" * 79)
        print()

    def player_name(self):
        """Return human player name."""
        return self._player_name

    def do_change_name(self, _):
        """Change player name."""
        old_name = self.player.get_name()
        new_name = input("Enter new nickname: ").lower()
        if new_name.lower() in self.h_score.high_score_dict:
            print("Name is already taken.")
        else:
            self.player.set_name(new_name)
            self.h_score.delete_name(old_name)

    def do_start(self, _):
        """Start the game."""
        shell1.Shell1(self.player).cmdloop()

    def do_rules(self, _):
        """Rules for pig game."""
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
        """Show high score."""
        self.h_score.save_current(self.player)
        self.h_score.get_high_score()

    def do_clear_high_score(self, _):
        """Clear the high score."""
        self.h_score.clear_dict()
        self.player.clear_player_stats(self.player)

    def do_exit(self, _):
        """Exit the program."""
        print("Exit the program")
        print("See you next time")
        self.h_score.save_current(self.player)
        self.h_score.save()
        return True

    def default(self, line):
        """Print error message when entering wrong command."""
        print("Wrong command. Type 'help' for a list of commands.")
