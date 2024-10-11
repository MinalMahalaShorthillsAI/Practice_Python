import unittest
from code import Solution  # Importing the Solution class

class TestIsSubsequence(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_cases(self):
        self.assertTrue(self.solution.isSubsequence("abc", "ahbgdc"))  # Example 1: should return True
        self.assertFalse(self.solution.isSubsequence("axc", "ahbgdc")) # Example 2: should return False

    def test_empty_s(self):
        self.assertTrue(self.solution.isSubsequence("", "ahbgdc"))    # An empty s should always be a subsequence
        self.assertTrue(self.solution.isSubsequence("", ""))           # Both empty strings

    def test_empty_t(self):
        self.assertFalse(self.solution.isSubsequence("abc", ""))      # Non-empty s cannot be a subsequence of empty t

    def test_full_match(self):
        self.assertTrue(self.solution.isSubsequence("abc", "abc"))     # s matches t exactly
        self.assertTrue(self.solution.isSubsequence("abc", "aabbcc"))  # s is a subsequence with extra characters

    def test_non_subsequence(self):
        self.assertFalse(self.solution.isSubsequence("abc", "ac"))     # Not in order
        self.assertFalse(self.solution.isSubsequence("abc", "bac"))    # Not in order
        self.assertFalse(self.solution.isSubsequence("abcd", "dcba"))  # Reverse order

    def test_long_subsequence(self):
        self.assertTrue(self.solution.isSubsequence("abcde", "abcdefghij"))  # Longer t, s is a subsequence

    def test_special_cases(self):
        self.assertTrue(self.solution.isSubsequence("a", "a"))         # Single character match
        self.assertFalse(self.solution.isSubsequence("a", "b"))        # Single character mismatch
        self.assertTrue(self.solution.isSubsequence("aaaa", "aaabaaa")) # Multiple characters with extra

if __name__ == '__main__':
    unittest.main()
