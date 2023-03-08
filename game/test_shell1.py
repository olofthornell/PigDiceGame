"Unit testing"
import unittest
from player import Player
from gameplay import Game
from dice import Dice
from old_shell1 import Shell


class TestShell1(unittest.TestCase):
    """Test shell1 class"""

    def setUp(self):
        name = "test_name"
        self.player = Player(name)
        self.game = Game()
        self.dice = Dice()

    def test_init_default_object(self):
        """Instantiate an object and check its properties."""
        res = Shell(self.player)
        exp = Shell
        self.assertIsInstance(res, exp)
