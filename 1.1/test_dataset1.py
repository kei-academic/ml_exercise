import unittest
from dataset1 import true_function

class TestDataset1(unittest.TestCase):
    """test class of dataset1.py
    """

    def test_true_function(self):
        """test method of true_function
        """
        x = 0
        expected_y = 0
        y = true_function(x)
        self.assertEqual(expected_y, y)

if __name__ == "__main__":
    unittest.main()
