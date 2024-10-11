import unittest
from code import Solution


class TestFindAndReplacePattern(unittest.TestCase):
    def setUp(self):
        # Assuming the Solution class has been imported correctly
        self.solution = Solution()

    def test_example_1(self):
        words = ["abc", "deq", "mee", "aqq", "dkd", "ccc"]
        pattern = "abb"
        expected_output = ["mee", "aqq"]
        actual_output = self.solution.findAndReplacePattern(words, pattern)
        self.assertTrue(set(expected_output).issubset(set(actual_output)))

    def test_example_2(self):
        words = ["a", "b", "c"]
        pattern = "a"
        expected_output = ["a", "b", "c"]
        actual_output = self.solution.findAndReplacePattern(words, pattern)
        self.assertTrue(set(expected_output).issubset(set(actual_output)))

    def test_no_matches(self):
        words = ["abc", "deq", "xyz"]
        pattern = "abb"
        expected_output = []
        actual_output = self.solution.findAndReplacePattern(words, pattern)
        self.assertEqual(actual_output, expected_output)

    def test_identical_pattern(self):
        words = ["aaa", "bbb", "ccc"]
        pattern = "xxx"
        expected_output = ["aaa", "bbb", "ccc"]
        actual_output = self.solution.findAndReplacePattern(words, pattern)
        self.assertTrue(set(expected_output).issubset(set(actual_output)))

    def test_single_word_match(self):
        words = ["abc"]
        pattern = "abc"
        expected_output = ["abc"]
        actual_output = self.solution.findAndReplacePattern(words, pattern)
        self.assertEqual(actual_output, expected_output)

    def test_multiple_same_length_no_match(self):
        words = ["abcd", "efgh", "ijkl"]
        pattern = "aabb"
        expected_output = []
        actual_output = self.solution.findAndReplacePattern(words, pattern)
        self.assertEqual(actual_output, expected_output)

    def test_pattern_with_same_characters(self):
        words = ["aa", "aaa", "aaaa"]
        pattern = "aa"
        expected_output = ["aa"]
        actual_output = self.solution.findAndReplacePattern(words, pattern)
        self.assertTrue(set(expected_output).issubset(set(actual_output)))

    def test_case_with_same_length_words(self):
        words = ["abcd", "efgh", "ijkl"]
        pattern = "aabb"
        expected_output = []
        actual_output = self.solution.findAndReplacePattern(words, pattern)
        self.assertEqual(actual_output, expected_output)

    def test_special_case_with_repeated_characters(self):
        words = ["aabb", "ccdd", "eeff", "gghh"]
        pattern = "xxyy"
        expected_output = ["aabb", "ccdd", "eeff", "gghh"]
        actual_output = self.solution.findAndReplacePattern(words, pattern)
        self.assertTrue(set(expected_output).issubset(set(actual_output)))

    def test_longest_pattern_and_words(self):
        words = ["abcdefghij", "klmnopqrst", "uvwxyzabcd"]
        pattern = "abcdefghij"
        expected_output = ["abcdefghij", "klmnopqrst", "uvwxyzabcd"]
        actual_output = self.solution.findAndReplacePattern(words, pattern)
        self.assertEqual(actual_output, expected_output)

if __name__ == '__main__':
    unittest.main()
