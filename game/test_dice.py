import unittest
from dice import Dice


class test_dice(unittest.TestCase):

    def test_roll(self):
        resault = Dice.roll(self)
        self.assertGreaterEqual(resault, 1)
        self.assertLessEqual(resault, 6)


if __name__ == "__main__":
    unittest.main()
