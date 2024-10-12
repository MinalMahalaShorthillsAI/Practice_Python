from code import Solution
import unittest

class TestminimumOperations(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        nums = [1, 2, 3, 4]
        expected = 3
        self.assertEqual(self.solution.minimumOperations(nums), expected)

    def test_example_2(self):
        nums = [3, 6, 9]
        expected = 0
        self.assertEqual(self.solution.minimumOperations(nums), expected)

    def test_all_elements_divisible_by_3(self):
        nums = [3, 6, 9, 12]
        expected = 0
        self.assertEqual(self.solution.minimumOperations(nums), expected)

    def test_all_elements_one_less_than_divisible_by_3(self):
        nums = [2, 5, 8, 11]
        expected = 4  # 1 for each element
        self.assertEqual(self.solution.minimumOperations(nums), expected)

    def test_all_elements_one_more_than_divisible_by_3(self):
        nums = [1, 4, 7, 10]
        expected = 4  # 1 for each element
        self.assertEqual(self.solution.minimumOperations(nums), expected)

    def test_mixed_elements(self):
        nums = [1, 2, 3, 4, 5]
        expected = 4  # 3 operations for 1, 1 for 2, and 1 for 4 and 1 for 5
        self.assertEqual(self.solution.minimumOperations(nums), expected)

    def test_large_elements(self):
        nums = [49, 50]
        expected = 2  # 1 for 49 (to 48), 1 for 50 (to 51)
        self.assertEqual(self.solution.minimumOperations(nums), expected)

    def test_single_element_divisible_by_3(self):
        nums = [9]
        expected = 0
        self.assertEqual(self.solution.minimumOperations(nums), expected)

    def test_single_element_not_divisible_by_3(self):
        nums = [10]
        expected = 1  # 1 operation to make 10 to 9 or 11
        self.assertEqual(self.solution.minimumOperations(nums), expected)

    def test_edge_case_with_min_length(self):
        nums = [1]
        expected = 1  # 1 operation to make 1 to 0 or 2
        self.assertEqual(self.solution.minimumOperations(nums), expected)

    def test_edge_case_with_max_length(self):
        nums = [1] * 50  # all elements are 1
        expected = 50  # 1 operation for each element
        self.assertEqual(self.solution.minimumOperations(nums), expected)

if __name__ == '__main__':
    unittest.main()
