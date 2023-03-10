"""Testing high_score class."""
import unittest
from high_score import HighScore
from player import Player


class TestHighScore(unittest.TestCase):
    """Test high score class."""

    def test_init_default_object(self):
        """Init high_score test."""
        res = HighScore()
        exp = HighScore
        self.assertIsInstance(res, exp)

    def test_move_player_info(self):
        """Testing move_player_info method."""
        pass

    def test_save_current(self):
        """Testing save_current method."""
        high_score = HighScore()
        test_player = Player("Hans")
        high_score.save_current(test_player)
        self.assertIn("Hans", high_score.high_score_dict)

    def test_delete_name(self):
        """Testing delete_name method."""
        high_score = HighScore()
        test_player = Player("Hans")
        high_score.save_current(test_player)
        high_score.delete_name(test_player)
        res = high_score.get_high_score()
        exp = None
        self.assertEqual(res, exp)


if __name__ == "__main__":
    unittest.main()
