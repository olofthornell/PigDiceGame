"""Unit testing gameplay."""
import unittest
from pig.dice import Dice
from pig.player import Player
from pig.game import Game


class TestGame(unittest.TestCase):
    """Test gamep class."""

    def setUp(self):
        """Set up player."""
        name = "test_name"
        self.player = Player(name)
        self.game = Game()
        self.dice = Dice()

    def test_init_object(self):
        """Instantiate an object and check its properties."""
        res = Game()
        exp = Game
        self.assertIsInstance(res, exp)

    def test_turn(self):
        """Test turn."""
        self.player.roll_score = self.dice.get_dice_min
        self.player.turn_score = self.dice.get_dice_max()
        self.game.turn(self.player)
        self.assertEqual(self.player.turn_score, 0)

        self.player.turn_score = 10
        self.player.roll_score = 1
        self.game.turn(self.player)
        self.assertEqual(0, self.player.turn_score)

        self.player.roll_score = 3
        self.player.turn_score = 3
        self.game.turn(self.player)
        self.assertEqual(self.player.turn_score, 6)

    def test_total(self):
        """Test total."""
        self.player.turn_score = 6
        self.player.total_score = 5
        self.game.total(self.player)
        self.assertEqual(self.player.total_score, 11)

    def test_cheat(self):
        """Test cheat."""
        self.game.cheat(self.player)
        self.assertEqual(self.player.roll_score, self.dice.get_dice_max())

    def test_roll(self):
        """Test roll."""
        self.game.roll(self.player)
        resault = self.player.roll_score
        expected = self.dice.get_dice_min()\
            <= resault <= self.dice.get_dice_max()
        self.assertTrue(expected)


if __name__ == "__main__":
    unittest.main()
