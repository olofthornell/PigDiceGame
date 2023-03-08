#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Unit testing."""

import unittest
from guess import the_game


class TestGameClass(unittest.TestCase):
    """Test the class."""

    def test_init_default_object(self):
        """Instantiate an object and check its properties."""
        res = the_game.Game()
        exp = the_game.Game
        self.assertIsInstance(res, exp)

    def test_start_the_game(self):
        """Roll a dice and check value is in bounds."""
        the_game = the_game.Game()
        the_game.start()

        res = the_game.the_number
        exp = the_game.low_number <= res <= the_game.high_number
        self.assertTrue(exp)


if __name__ == "__main__":
    unittest.main()
