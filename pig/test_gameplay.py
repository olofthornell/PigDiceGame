"""Test gameplay class."""
import unittest

import time
from pig.game import Game
from pig.player import Player
from pig.gameplay import Gameplay
from pig.intelligence import Intelligence


class TestGameplay(unittest.TestCase):
    """Test gameplay class."""

    def setUp(self):
        """Test setting up player."""
        name = "test_name"
        self.human_player = Player(name)
        self.computer_player = Player("cpu")
        self.game = Game()
        self.intell = Intelligence()
        self.current_player = self.computer_player
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

        self.gameplay.switch_player()
        self.assertIs(self.current_player, self.computer_player)

    def test_set_difficulty(self):
        """Set and check difficulty on cpu."""
        self.gameplay.set_difficulty("coward")
        self.assertEqual(self.gameplay.difficulty, self.intell.get_coward())

        self.gameplay.set_difficulty("moderate")
        self.assertEqual(self.gameplay.difficulty, self.intell.get_moderate())

        self.gameplay.set_difficulty("bold")
        self.assertEqual(self.gameplay.difficulty, self.intell.get_bold())

    def test_get_current_player(self):
        """Check if current player is instance of player class."""
        curr_player = self.gameplay.get_current_player()
        self.assertIsInstance(curr_player, Player)

    def test_short_pause(self):
        """Check length on short pause."""
        start_time = time.time()
        self.gameplay.short_pause()
        end_time = time.time()
        self.assertAlmostEqual(end_time - start_time, 0.4, delta=0.1)

    def test_medium_pause(self):
        """Check length on short pause."""
        start_time = time.time()
        self.gameplay.medium_pause()
        end_time = time.time()
        self.assertAlmostEqual(end_time - start_time, 1, delta=0.1)

    def test_long_pause(self):
        """Check length on short pause."""
        start_time = time.time()
        self.gameplay.long_pause()
        end_time = time.time()
        self.assertAlmostEqual(end_time - start_time, 2, delta=0.1)

    def test_roll(self):
        """Test roll and turn score."""
        self.gameplay.roll()
        self.assertGreaterEqual(self.current_player.roll_score, 0)
        self.assertLessEqual(self.current_player.roll_score, 6)

        self.assertGreaterEqual(self.current_player.turn_score, 0)
        self.assertLessEqual(self.current_player.turn_score, 6)


if __name__ == "__main__":
    unittest.main()
