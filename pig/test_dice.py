"""Unit testing dice."""

import unittest
from pig.dice import Dice


class TestDice(unittest.TestCase):
    """Test the dice class."""

    def setUp(self):
        """Create dice."""
        self.dice = Dice()

    def test_init_object(self):
        """Instantiate an object and check its properties."""
        res = Dice()
        exp = Dice
        self.assertIsInstance(res, exp)

    def test_roll(self):
        """Test range on dice value."""
        resault = self.dice.roll()
        self.assertGreaterEqual(resault, 1)
        self.assertLessEqual(resault, 6)

    def test_get_dice_min(self):
        """Test."""
        exp = self.dice.dice_min
        res = self.dice.get_dice_min()
        self.assertEqual(exp, res)

    def test_get_dice_max(self):
        """Test dice max."""
        exp = self.dice.dice_max
        res = self.dice.get_dice_max()
        self.assertEqual(exp, res)


if __name__ == "__main__":
    unittest.main()
