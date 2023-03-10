"""Unit testing intelligence."""
import unittest
from pig.intelligence import Intelligence


class TestIntelligence(unittest.TestCase):
    """Test intelligence class."""

    def setUp(self):
        """Test setting up cpu."""
        self.intelligence = Intelligence()

    def test_init_object(self):
        """Instantiate an object and check its properties."""
        res = Intelligence()
        exp = Intelligence
        self.assertIsInstance(res, exp)

    def test_coward(self):
        """Check limit, value of coward variable."""
        exp = self.intelligence.coward
        res = self.intelligence.get_coward()
        self.assertEqual(exp, res)

    def test_moderate(self):
        """Check limit, value of moderate variable."""
        exp = self.intelligence.moderate
        res = self.intelligence.get_moderate()
        self.assertEqual(exp, res)

    def test_bold(self):
        """Check limit, value of bold variable."""
        exp = self.intelligence.bold
        res = self.intelligence.get_bold()
        self.assertEqual(exp, res)


if __name__ == "__main__":
    unittest.main()
