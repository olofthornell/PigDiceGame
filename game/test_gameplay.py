import unittest
from gameplay import Game
from dice import Dice
from player import Player


class test_game(unittest.TestCase):

    def setUp(self):
        name = "test_name"
        player = Player(name)
        self.game = Game(player)
        self.dice = Dice()

    def test_turn(self):
        self.game.roll_score = self.dice.dice_min()
        self.game.turn_score = self.dice.dice_max()
        self.game.turn()
        self.assertEqual(self.game.turn_score, 0)

    def test_total(self):
        self.game.turn_score = 6
        self.game.total_score = 5
        self.game.total()
        self.assertEqual(self.game.total_score, 11)
        
    def test_cheat(self):
        self.game.cheat()
        self.assertEqual(self.game.turn_score, self.dice.dice_max())
        
    def test_roll(self):
        self.game.roll()
        resault = self.game.roll_score
        expected = self.dice.dice_min() <= resault <= self.dice.dice_max()
        self.assertTrue(expected)


if __name__ == "__main__":
    unittest.main()
