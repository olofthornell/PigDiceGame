"""Test gameplay class."""
import unittest

from game.game import Game
from game.player import Player
from game.gameplay import Gameplay


class TestGameplay(unittest.TestCase):
    """Test gameplay class."""

    def setUp(self):
        """Test setting up player."""
        name = "test_name"
        self.human_player = Player(name)
        self.computer_player = Player("cpu")
        self.game = Game()
        self.current_player = self.human_player
        self.gameplay = Gameplay(self.current_player)

    def test_init_object(self):
        """Instantiate an object and check its properties."""
        res = Gameplay(self.current_player)
        exp = Gameplay
        self.assertIsInstance(res, exp)

    def test_swich_player(self):
        """Switch between computer and human player."""
        self.gameplay.switch_player()
        self.assertIs(self.current_player, self.computer_player)

        self.gameplay.switch_player
        self.assertIs(self.current_player, self.computer_player)


if __name__ == "__main__":
    unittest.main()
