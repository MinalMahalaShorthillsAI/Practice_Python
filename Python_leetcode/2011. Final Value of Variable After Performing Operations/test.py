import unittest
from code import Solution  # Importing the Solution class from solution.py

class TestFinalValueAfterOperations(unittest.TestCase):
    
    def setUp(self):
        self.solution = Solution()

    def test_basic_operations(self):
        self.assertEqual(self.solution.finalValueAfterOperations(["--X", "X++", "X++"]), 1)

    def test_all_increments(self):
        self.assertEqual(self.solution.finalValueAfterOperations(["++X", "++X", "X++"]), 3)

    def test_mixed_operations_leading_to_zero(self):
        self.assertEqual(self.solution.finalValueAfterOperations(["X++", "++X", "--X", "X--"]), 0)

    def test_only_decrements(self):
        self.assertEqual(self.solution.finalValueAfterOperations(["--X", "X--", "--X"]), -3)

    def test_equal_increments_and_decrements(self):
        self.assertEqual(self.solution.finalValueAfterOperations(["++X", "X++", "--X", "X--"]), 0)

    def test_all_operations_leading_to_positive_value(self):
        self.assertEqual(self.solution.finalValueAfterOperations(["X++", "++X", "X++", "X++"]), 4)

    def test_no_operations(self):
        self.assertEqual(self.solution.finalValueAfterOperations([]), 0)

    def test_maximum_constraints_with_alternating_operations(self):
        self.assertEqual(self.solution.finalValueAfterOperations(["++X", "X--"] * 50), 0)

    def test_all_X_plus_plus_operations(self):
        self.assertEqual(self.solution.finalValueAfterOperations(["X++"] * 100), 100)

    def test_all_X_minus_minus_operations(self):
        self.assertEqual(self.solution.finalValueAfterOperations(["--X"] * 100), -100)

if __name__ == '__main__':
    unittest.main()
