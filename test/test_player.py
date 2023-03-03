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


if __name__ == "__main__":
    unittest.main()