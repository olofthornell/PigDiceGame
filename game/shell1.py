import cmd
from gameplay import Game
from player import Player


class Shell(cmd.Cmd):

    def __init__(self, player_name):
        """Init game and player objects."""
        super().__init__()
        self.human_player = Player(player_name)
        self.computer_player = Player("cPIGu")
        self._current_player = self.human_player
        self.game1 = Game()
        self.win_point = 100
        print()
        print(f"First player is {self._current_player.get_name()}!")
        print("-" * 37)
        print()
        
    def current_player(self):
        """Returning the current player"""
        return self._current_player
        
    def switch_player(self):
        """Switch between human player and cpu"""
        if self._current_player == self.human_player:
            self._current_player = self.computer_player
            # cPIGu playes
        else:
            self._current_player = self.human_player
        print()
        print("-" * 37)
        print(f"Next player is {self._current_player.get_name()}!")
        print(f"You're total is {self._current_player.get_total_score()}")
        print("-" * 37)
        print()
            
    def do_cheat(self, _):
        """Roll the dice and get a six"""
        self.game1.cheat(self._current_player)
        self.game1.turn(self._current_player)
        print("Well look at that - you rolled a six...")
        print(f"Turn score: {self._current_player.get_turn_score()}")
        
    def do_roll(self, _):
        """Roll dice and add score to turn and print resault"""
        print(f"{self.current_player().get_name()}")
        self.game1.roll(self._current_player)
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
        if self._current_player.get_total_score() >= self.win_point:
            print(f"{self._current_player} is the winner!!!")
            return self.do_exit(exit)
            
    def do_hold(self, _):
        self.game1.hold(self._current_player)
        self.switch_player()
        # cPIGu
        
    def do_total(self, _):
        print(f"{self._current_player.get_name()}")
        print(f"{self._current_player.get_total_score()}")

    def do_exit(self, _):
        print("Well played! Bye")
        return True
