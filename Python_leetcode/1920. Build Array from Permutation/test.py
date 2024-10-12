import unittest
from code import Solution
class Solution(object):
    def buildArray(self, nums):
        return [nums[nums[i]] for i in range(len(nums))]

class TestBuildArray(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        nums = [0, 2, 1, 5, 3, 4]
        expected = [0, 1, 2, 4, 5, 3]
        self.assertEqual(self.solution.buildArray(nums), expected)

    def test_example_2(self):
        nums = [5, 0, 1, 2, 3, 4]
        expected = [4, 5, 0, 1, 2, 3]
        self.assertEqual(self.solution.buildArray(nums), expected)

    def test_single_element(self):
        nums = [0]
        expected = [0]
        self.assertEqual(self.solution.buildArray(nums), expected)

    def test_two_elements(self):
        nums = [1, 0]
        expected = [0, 1]
        self.assertEqual(self.solution.buildArray(nums), expected)

    def test_three_elements(self):
        nums = [2, 0, 1]
        expected = [1, 2, 0]
        self.assertEqual(self.solution.buildArray(nums), expected)

    def test_reverse_order(self):
        nums = [3, 2, 1, 0]
        expected = [0, 1, 2, 3]
        self.assertEqual(self.solution.buildArray(nums), expected)

    def test_large_permutation(self):
        nums = list(range(1000))
        expected = list(range(1000))
        self.assertEqual(self.solution.buildArray(nums), expected)

    def test_random_permutation(self):
        nums = [3, 0, 2, 1]
        expected = [1, 3, 2, 0]
        self.assertEqual(self.solution.buildArray(nums), expected)

    def test_all_elements_pointing_to_self(self):
        nums = [0, 1, 2, 3]
        expected = [0, 1, 2, 3]
        self.assertEqual(self.solution.buildArray(nums), expected)

    def test_circular_reference(self):
        nums = [1, 2, 0]
        expected = [2, 0, 1]
        self.assertEqual(self.solution.buildArray(nums), expected)

    def test_non_sequential_elements(self):
        nums = [4, 3, 2, 1, 0]
        expected = [0, 1, 2, 3, 4]
        self.assertEqual(self.solution.buildArray(nums), expected)

    def test_large_random_permutation(self):
        nums = [2, 0, 4, 1, 3]
        expected = [4, 2, 3, 0, 1]
        self.assertEqual(self.solution.buildArray(nums), expected)

    def test_single_swapped_elements(self):
        nums = [1, 0, 3, 2]
        expected = [0, 1, 2, 3]
        self.assertEqual(self.solution.buildArray(nums), expected)

if __name__ == '__main__':
    unittest.main()
