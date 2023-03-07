import unittest
from game import player


class TestPlayerClass(unittest.TestCase):

    def test_init_default_object(self):
        res = player.Player("Name")
        exp = player.Player
        self.assertIsInstance(res, exp)

    def test_get_name(self):
        test_player = player.Player("Name")
        res = test_player.get_name()
        exp = "Name"
        self.assertEqual(res, exp)

    def test_set_name(self):
        test_player = player.Player("Name")
        test_player.set_name("Name1")
        res = test_player.name
        exp = "Name1"
        self.assertEqual(res, exp)

    def test_get_wins(self):
        test_player = player.Player("Name")
        res = test_player.get_wins()
        exp = 0
        self.assertEqual(res, exp)

    def test_set_wins(self):
        test_player = player.Player("Name")
        test_player.set_wins(3)
        res = test_player.wins
        exp = 3
        self.assertEqual(res, exp)

    def test_add_wins(self):
        test_player = player.Player("Name")
        test_player.add_win
        res = test_player.wins
        exp = test_player.get_wins()
        self.assertEqual(res, exp)

    def test_get_roll_score(self):
        test_player = player.Player("Name")
        res = test_player.get_roll_score()
        exp = 0
        self.assertEqual(res, exp)

    def test_set_roll_score(self):
        test_player = player.Player("Name")
        test_player.set_roll_score(3)
        res = test_player.roll_score
        exp = 3
        self.assertEqual(res, exp)

    def test_get_turn_score(self):
        test_player = player.Player("Name")
        res = test_player.get_turn_score()
        exp = 0
        self.assertEqual(res, exp)

    def test_set_turn_score(self):
        test_player = player.Player("Name")
        test_player.set_turn_score(3)
        res = test_player.turn_score
        exp = 3
        self.assertEqual(res, exp)

    def test_get_total_score(self):
        test_player = player.Player("Name")
        res = test_player.get_total_score()
        exp = 0
        self.assertEqual(res, exp)

    def test_set_total_score(self):
        test_player = player.Player("Name")
        test_player.set_total_score(3)
        res = test_player.total_score
        exp = 3
        self.assertEqual(res, exp)

    def test_get_games_played(self):
        test_player = player.Player("Name")
        res = test_player.get_games_played()
        exp = 0
        self.assertEqual(res, exp)

    def test_set_games_played(self):
        test_player = player.Player("Name")
        test_player.set_games_played(3)
        res = test_player.games_played
        exp = 3
        self.assertEqual(res, exp)

    def test_add_games_played(self):
        test_player = player.Player("Name")
        test_player.add_games_played
        res = test_player.games_played
        exp = test_player.get_games_played()
        self.assertEqual(res, exp)


if __name__ == "__main__":
    unittest.main()
