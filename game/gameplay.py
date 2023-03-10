"""Gameplay mechanics for Pig game."""

import time
from intelligence import Intelligence
from player import Player
from game import Game


class Gameplay:
    """Gameplay for Pig game."""

    def __init__(self, player):
        """Init game and player objects."""
        self.intell = Intelligence()
        self.difficulty = self.intell.get_moderate()
        self.human_player = player
        self.computer_player = Player("cPIGu")
        self.current_player = self.human_player
        self.game1 = Game()
        self.win_point = 100
        self.print_menu()

    def print_menu(self):
        """Print in game menu."""
        print('\n' * 2)
        print("In game commands:")
        print("-" * 79)
        print(f"{'roll':20}| Roll the dice")
        print("-" * 79)
        print(f"{'hold':20}| Save your score to the total and end your turn")
        print("-" * 79)
        print(f"{'cheat':20}| Loose your soul for fame and glory")
        print("-" * 79)
        print(f"{'difficulty coward':20}| Opponent cPIGu is a coward")
        print("-" * 79)
        print(f"{'difficulty moderate':20}| Opponent cPIGu is moderate"
              " (default)")
        print("-" * 79)
        print(f"{'difficulty bold':20}| Opponent cPIGu is bold")
        print("-" * 79)
        print(f"{'help':20}| Show list of commands")
        print("-" * 79)
        print(f"{'exit':20}| Return to main menu")
        print("-" * 79)
        print()
        print(f"First player is {self.current_player.get_name()}!")
        print()

    def set_difficulty(self, arg):
        """Choose personality on opponent cPIGu."""
        if arg == "coward":
            print("cPIGu personality set to 'coward'")
            self.difficulty = self.intell.get_coward()
        if arg == "moderate":
            print("cPIGu personality set to 'moderate'")
            self.difficulty = self.intell.get_moderate()
        if arg == "bold":
            print("cPIGu personality set to 'bold'")
            self.difficulty = self.intell.get_bold()

    def get_current_player(self):
        """Return the current player."""
        return self.current_player

    def switch_player(self):
        """Switch between human player and cpu player."""
        if self.current_player == self.human_player:
            self.current_player = self.computer_player
            print()
            print("-" * 79)
            print(f"Next player is {self.current_player.get_name()}!")
            print(f"You're total is {self.current_player.get_total_score()}")
            print("-" * 79)
            print()
            self.cpigu_roll()
        else:
            self.current_player = self.human_player
            print()
            print("-" * 79)
            print(f"Next player is {self.current_player.get_name()}!")
            print(f"You're total is {self.current_player.get_total_score()}")
            print("-" * 79)
            print()

    def cpigu_roll(self):
        """Cpu player roll the dice."""
        self.game1.roll(self.current_player)
        self.turn()
        while self.computer_player.get_roll_score() != 1\
                and self.computer_player.get_turn_score()\
                < self.difficulty:
            self.medium_pause()
            self.game1.roll(self.current_player)
            self.turn()
        if self.current_player == self.computer_player:
            self.game1.hold(self.current_player)
            self.switch_player()

    def cheat(self):
        """Roll the dice and get max value of the dice."""
        print(f"{self.current_player().get_name()}")
        self.game1.cheat(self.current_player)
        self.turn()

    def roll(self):
        """Roll the dice."""
        self.short_pause()
        print()
        print(f"{self.current_player.get_name()}")
        self.game1.roll(self.current_player)
        self.turn()

    def turn(self):
        """Print score for turn and total.

        If dice score is 1, player is switched and score turn 0.
        If score i 100 game ends.
        """
        self.game1.turn(self.current_player)
        roll = self.current_player.get_roll_score()
        turn = self.current_player.get_turn_score()
        total = self.current_player.get_total_score()
        print(f"You rolled a {roll}")
        print(f"Turn score: {turn}")
        print(f"Total score: {total + turn}")
        print()
        if self.current_player.get_roll_score() == 1:
            print(f"Oh no! You rolled a {roll}")
            self.long_pause()
            self.switch_player()
        if total + turn >= self.win_point:
            self.game1.total(self.current_player)
            print(f"{self.current_player.get_name()} is the winner!!!")
            print()
            print("Enter 'exit' to return to main menu")
            print("Enter 'roll' to start a new game")
            print("Enter 'help' for a list of commands")
            print()
            self.current_player.add_win()
            self.human_player.add_games_played()
            self.computer_player.set_roll_score(1)
            self.computer_player.set_turn_score(0)
            self.computer_player.set_total_score(0)
            self.human_player.set_turn_score(0)
            self.human_player.set_total_score(0)
            self.current_player = self.human_player

    def short_pause(self):
        """Pause the game short time."""
        time.sleep(0.4)

    def medium_pause(self):
        """Pause the game medium time."""
        time.sleep(1)

    def long_pause(self):
        """Pause the game long time."""
        time.sleep(2)

    def hold(self):
        """End turn and collect points."""
        self.medium_pause()
        self.game1.hold(self.current_player)
        self.switch_player()
