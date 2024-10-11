import unittest
from code import Solution  # Importing the Solution class

class TestScoreOfString(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_cases(self):
        self.assertEqual(self.solution.scoreOfString("hello"), 13)  # Example 1
        self.assertEqual(self.solution.scoreOfString("zaz"), 50)     # Example 2

    def test_min_length(self):
        self.assertEqual(self.solution.scoreOfString("ab"), 1)       # |b-a| = 1
        self.assertEqual(self.solution.scoreOfString("az"), 25)      # |z-a| = 25

    def test_repeated_characters(self):
        self.assertEqual(self.solution.scoreOfString("aaaa"), 0)     # All same characters
        self.assertEqual(self.solution.scoreOfString("abcabc"), 6)   # |b-a| + |c-b| + |a-c| + |b-a| + |c-b| = 6

    def test_alternating_characters(self):
        self.assertEqual(self.solution.scoreOfString("abab"), 3)      # |b-a| + |a-b| + |b-a| = 2
        self.assertEqual(self.solution.scoreOfString("azaz"), 75)     # |z-a| + |a-z| + |z-a| = 50

    def test_edge_cases(self):
        self.assertEqual(self.solution.scoreOfString("bc"), 1)        # |c-b| = 1
        self.assertEqual(self.solution.scoreOfString("yx"), 1)        # |x-y| = 1

    def test_long_string(self):
        self.assertEqual(self.solution.scoreOfString("a" * 100), 0)  # Long string of the same character
        self.assertEqual(self.solution.scoreOfString("abcdef"), 5)    # |b-a| + |c-b| + |d-c| + |e-d| + |f-e| = 5

if __name__ == '__main__':
    unittest.main()
