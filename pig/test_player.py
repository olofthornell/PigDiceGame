"""Testing player class."""
import unittest
from pig.player import Player


class TestPlayerClass(unittest.TestCase):
    """Creating test for player."""

    def test_init_default_object(self):
        """Init player test."""
        res = Player("Name")
        exp = Player
        self.assertIsInstance(res, exp)

    def test_get_name(self):
        """Testing name getter."""
        test_player = Player("Name")
        res = test_player.get_name()
        exp = "Name"
        self.assertEqual(res, exp)

    def test_set_name(self):
        """Testing name setter."""
        test_player = Player("Name")
        test_player.set_name("Name1")
        res = test_player.name
        exp = "Name1"
        self.assertEqual(res, exp)

    def test_get_wins(self):
        """Testing wins getter."""
        test_player = Player("Name")
        res = test_player.get_wins()
        exp = 0
        self.assertEqual(res, exp)

    def test_set_wins(self):
        """Testing wins setter."""
        test_player = Player("Name")
        test_player.set_wins(3)
        res = test_player.wins
        exp = 3
        self.assertEqual(res, exp)

    def test_add_wins(self):
        """Testing add winns."""
        test_player = Player("Name")
        res = test_player.wins
        exp = test_player.get_wins()
        self.assertEqual(res, exp)

    def test_get_roll_score(self):
        """Testing roll_score getter."""
        test_player = Player("Name")
        res = test_player.get_roll_score()
        exp = 0
        self.assertEqual(res, exp)

    def test_set_roll_score(self):
        """Testing roll_score setter."""
        test_player = Player("Name")
        test_player.set_roll_score(3)
        res = test_player.roll_score
        exp = 3
        self.assertEqual(res, exp)

    def test_get_turn_score(self):
        """Testing turn_score getter."""
        test_player = Player("Name")
        res = test_player.get_turn_score()
        exp = 0
        self.assertEqual(res, exp)

    def test_set_turn_score(self):
        """Testing turn_score setter."""
        test_player = Player("Name")
        test_player.set_turn_score(3)
        res = test_player.turn_score
        exp = 3
        self.assertEqual(res, exp)

    def test_get_total_score(self):
        """Testing total_score getter."""
        test_player = Player("Name")
        res = test_player.get_total_score()
        exp = 0
        self.assertEqual(res, exp)

    def test_set_total_score(self):
        """Testing total_score setter."""
        test_player = Player("Name")
        test_player.set_total_score(3)
        res = test_player.total_score
        exp = 3
        self.assertEqual(res, exp)

    def test_get_games_played(self):
        """Testing games_played getter."""
        test_player = Player("Name")
        res = test_player.get_games_played()
        exp = 0
        self.assertEqual(res, exp)

    def test_set_games_played(self):
        """Testing games_played setter."""
        test_player = Player("Name")
        test_player.set_games_played(3)
        res = test_player.games_played
        exp = 3
        self.assertEqual(res, exp)

    def test_add_games_played(self):
        """Testing add games_played."""
        test_player = Player("Name")
        test_player.add_games_played()
        res = test_player.games_played
        exp = test_player.get_games_played()
        self.assertEqual(res, exp)

    def test_clear_player_stats(self):
        """Testing clear_player_stats."""
        test_player = Player("Name")
        test_player.add_games_played()
        test_player.clear_player_stats(test_player)
        res = test_player.games_played
        exp = test_player.get_games_played()
        self.assertEqual(res, exp)


if __name__ == "__main__":
    unittest.main()
