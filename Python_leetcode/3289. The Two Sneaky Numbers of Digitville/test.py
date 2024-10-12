import unittest
from code import Solution

class TestFindDuplicates(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        nums = [0, 1, 1, 0]
        expected = [1, 0]
        self.assertEqual(self.solution.getSneakyNumbers(nums), expected)

    def test_example_2(self):
        nums = [0, 3, 2, 1, 3, 2]
        expected = [3, 2]
        self.assertEqual(self.solution.getSneakyNumbers(nums), expected)

    def test_example_3(self):
        nums = [7, 1, 5, 4, 3, 4, 6, 0, 9, 5, 8, 2]
        expected = [4, 5]
        self.assertEqual(self.solution.getSneakyNumbers(nums), expected)

    def test_two_consecutive_duplicates(self):
        nums = [0, 1, 1, 2, 2]
        expected = [1, 2]
        self.assertEqual(self.solution.getSneakyNumbers(nums), expected)

    def test_duplicates_at_ends(self):
        nums = [2, 3, 4, 0, 2, 1, 3]
        expected = [2, 3]
        self.assertEqual(self.solution.getSneakyNumbers(nums), expected)

    def test_large_numbers_with_duplicates(self):
        nums = [10, 20, 30, 10, 40, 20]
        expected = [10, 20]
        self.assertEqual(self.solution.getSneakyNumbers(nums), expected)

    def test_with_max_range(self):
        nums = [0, 1, 2, 3, 4, 4, 5, 6, 7, 8, 9]
        expected = [4]
        self.assertEqual(self.solution.getSneakyNumbers(nums), expected)

    def test_empty_slots(self):
        nums = [1, 2, 3, 2, 4, 5, 3]
        expected = [2, 3]
        self.assertEqual(self.solution.getSneakyNumbers(nums), expected)

    def test_non_sequential_numbers(self):
        nums = [6, 7, 8, 6, 5, 4, 7]
        expected = [6, 7]
        self.assertEqual(self.solution.getSneakyNumbers(nums), expected)

    def test_minimal_case(self):
        nums = [0, 0]
        expected = [0]
        self.assertEqual(self.solution.getSneakyNumbers(nums), expected)

if __name__ == '__main__':
    unittest.main()