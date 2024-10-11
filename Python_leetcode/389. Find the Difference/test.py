import unittest
from code import Solution  # Importing the Solution class

class TestFindTheDifference(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_cases(self):
        self.assertEqual(self.solution.findTheDifference("abcd", "abcde"), "e")  # Example 1
        self.assertEqual(self.solution.findTheDifference("", "y"), "y")          # Example 2

    def test_single_character(self):
        self.assertEqual(self.solution.findTheDifference("a", "aa"), "a")        # Single character added
        self.assertEqual(self.solution.findTheDifference("b", "ab"), "a")        # Single character added

    def test_multiple_characters(self):
        self.assertEqual(self.solution.findTheDifference("abc", "abcf"), "f")    # 'f' is added
        self.assertEqual(self.solution.findTheDifference("xyz", "xyza"), "a")    # 'a' is added

    def test_repeated_characters(self):
        self.assertEqual(self.solution.findTheDifference("aabb", "aabbb"), "b")  # 'b' is added
        self.assertEqual(self.solution.findTheDifference("cc", "cce"), "e")      # 'e' is added

    def test_large_input(self):
        self.assertEqual(self.solution.findTheDifference("a" * 1000, "a" * 1000 + "b"), "b")  # Large case

if __name__ == '__main__':
    unittest.main()
