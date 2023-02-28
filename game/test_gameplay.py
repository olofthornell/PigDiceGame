import unittest
from gameplay import Game
from dice import Dice


class test_game(unittest.TestCase):

    def setUp(self):
        self.game = Game()
        self.dice = Dice()

    def test_turn(self):
        self.game.roll_score = 1
        self.game.turn_score = 6
        self.game.turn()
        self.assertEqual(self.game.turn_score, 0)

    def test_total(self):
        self.game.turn_score = 6
        self.game.total_score = 5
        self.game.total()
        self.assertEqual(self.game.total_score, 11)
        
    def test_cheat(self):
        self.game.turn_score = 0
        self.game.cheat()
        self.assertEqual(self.game.turn_score, 6)
        
    def test_roll(self):
        self.dice.roll()
        resault = self.game.roll_score 
        expected = 1 
        
        



if __name__ == "__main__":
    unittest.main()