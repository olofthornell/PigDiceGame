"""Gameplay mechanics for Pig game"""

from game import Game
from player import Player
from intelligence import Intelligence


class Gameplay:
    """Gameplay for Pig game"""

    def __init__(self, player):
        """Init game and player objects."""
        self.intell = Intelligence()
        self._end_turn = False
        self._difficulty = self.intell.moderate()
        self.human_player = player
        self.computer_player = Player("cPIGu")
        self._current_player = self.human_player
        self.game1 = Game()
        self.win_point = 100
        self.print_menu()

    def print_menu(self):
        """Print in game menu"""
        print()
        print("In game commands:")
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
        print("-" * 79)
        print(f"First player is {self._current_player.get_name()}!")
        print("-" * 79)
        print()

    def difficulty(self, arg):
        """Choose personality on opponent cPIGu"""
        if arg == "coward":
            print("cPIGu personality set to 'coward'")
            self._difficulty = self.intell.coward()
        if arg == "moderate":
            print("cPIGu personality set to 'moderate'")
            self._difficulty = self.intell.moderate()
        if arg == "bold":
            print("cPIGu personality set to 'bold'")
            self._difficulty = self.intell.bold()

    def current_player(self):
        """Returning the current player"""
        return self._current_player

    def switch_player(self):
        """Switch between human player and cpu player"""
        if self._current_player == self.human_player:
            self._current_player = self.computer_player
            print()
            print("-" * 79)
            print(f"Next player is {self._current_player.get_name()}!")
            print(f"You're total is {self._current_player.get_total_score()}")
            print("-" * 79)
            print()
            self.cpigu_roll()
        else:
            self._current_player = self.human_player
            print()
            print("-" * 79)
            print(f"Next player is {self._current_player.get_name()}!")
            print(f"You're total is {self._current_player.get_total_score()}")
            print("-" * 79)
            print()

    def cpigu_roll(self):
        """The cpu player rolles the dice"""
        self.game1.roll(self._current_player)
        self.turn()
        if self._end_turn:
            return True
        else:
            while self.computer_player.get_roll_score() != 1\
                    and self.computer_player.get_turn_score()\
                    < self._difficulty:
                self.game1.roll(self._current_player)
                self.turn()
        if self._current_player == self.computer_player:
            self.game1.hold(self._current_player)
            self.switch_player()

    def cheat(self):
        """Roll the dice and get a six"""
        print(f"{self.current_player().get_name()}")
        self.game1.cheat(self._current_player)
        self.turn()
        if self._end_turn:
            return True

    def roll(self):
        """Roll the dice"""
        print()
        print(f"{self.current_player().get_name()}")
        self.game1.roll(self._current_player)
        self.turn()
        if self._end_turn:
            return True

    def turn(self):
        """Print score for turn and total.
        If dice score is 1, player is switched and score turn 0.
        If score i 100 game ends."""
        self.game1.turn(self._current_player)
        roll = self._current_player.get_roll_score()
        turn = self._current_player.get_turn_score()
        total = self._current_player.get_total_score()
        print(f"You rolled a {roll}")
        print(f"Turn score: {turn}")
        print(f"Total score: {total + turn}")
        print()
        if self._current_player.get_roll_score() == 1:
            print(f"Oh no! You rolled a {roll}")
            self.switch_player()
        if total + turn >= self.win_point:
            self.game1.total(self._current_player)
            print(f"{self._current_player.get_name()} is the winner!!!")
            self._current_player.add_win()
            self.human_player.add_games_played()
            self.computer_player.set_turn_score(0)
            self.computer_player.set_total_score(0)
            self.human_player.set_turn_score(0)
            self.human_player.set_total_score(0)
            self._end_turn = True

    def hold(self):
        """End turn and collect points"""
        self.game1.hold(self._current_player)
        self.switch_player()
