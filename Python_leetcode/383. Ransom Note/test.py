import unittest
from code import Solution  # Importing the Solution class

class TestCanConstruct(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_cases(self):
        self.assertFalse(self.solution.canConstruct("a", "b"))        # Example 1: Output should be False
        self.assertFalse(self.solution.canConstruct("aa", "ab"))      # Example 2: Output should be False
        self.assertTrue(self.solution.canConstruct("aa", "aab"))      # Example 3: Output should be True

    def test_empty_cases(self):
        self.assertTrue(self.solution.canConstruct("", "anything"))    # Empty ransomNote can be constructed
        self.assertFalse(self.solution.canConstruct("a", ""))          # Non-empty ransomNote cannot be constructed from empty magazine

    def test_edge_cases(self):
        self.assertTrue(self.solution.canConstruct("a", "aa"))        # Only one 'a' in magazine, not enough
        self.assertTrue(self.solution.canConstruct("b", "b"))          # Single character match
        self.assertFalse(self.solution.canConstruct("b", "a"))         # Single character mismatch

    def test_large_cases(self):
        self.assertTrue(self.solution.canConstruct("a" * 100000, "a" * 100000))  # Large case with enough characters
        self.assertFalse(self.solution.canConstruct("a" * 100001, "a" * 100000)) # Large case with not enough characters

    def test_variety_of_characters(self):
        self.assertTrue(self.solution.canConstruct("abc", "abcdef"))  # All characters present
        self.assertFalse(self.solution.canConstruct("abc", "ab"))     # Missing character 'c'

if __name__ == '__main__':
    unittest.main()
