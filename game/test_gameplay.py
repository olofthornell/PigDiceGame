<<<<<<< HEAD
import unittest
from gameplay import Game


class test_game(unittest.TestCase):

    def setUp(self):
        self.game = Game()

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



if __name__ == "__main__":
=======
import unittest
from gameplay import Game


class test_game(unittest.TestCase):

    def setUp(self):
        self.game = Game()

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



if __name__ == "__main__":
>>>>>>> 494c811ec5dff1e99c696619e157de0bd380ae22
    unittest.main()