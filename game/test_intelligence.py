"""Unit testing intelligence"""
import unittest
from intelligence import Intelligence


class TestIntelligence(unittest.TestCase):
    "Test intelligence class"

    def setUp(self):
        self.intelligence = Intelligence()

    def test_init_object(self):
        """Instantiate an object and check its properties."""
        res = Intelligence()
        exp = Intelligence
        self.assertIsInstance(res, exp)

    def test_coward(self):
        """Check limit, value of coward variable"""
        exp = self.intelligence._coward
        res = self.intelligence.coward()
        self.assertEqual(exp, res)

    def test_moderate(self):
        """Check limit, value of moderate variable"""
        exp = self.intelligence._moderate
        res = self.intelligence.moderate()
        self.assertEqual(exp, res)

    def test_bold(self):
        """Check limit, value of bold variable"""
        exp = self.intelligence._bold
        res = self.intelligence.bold()
        self.assertEqual(exp, res)
