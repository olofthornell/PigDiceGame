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
        test_player = player.Player(5)
        res = test_player.get_wins()
        exp = 5
        self.assertEqual(res, exp)

    def test_set_wins(self):
        


if __name__ == "__main__":
    unittest.main()