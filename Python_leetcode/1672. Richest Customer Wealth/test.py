import unittest
from code import Solution

class TestMaximumWealth(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        accounts = [[1, 2, 3], [3, 2, 1]]
        expected = 6
        self.assertEqual(self.solution.maximumWealth(accounts), expected)

    def test_example_2(self):
        accounts = [[1, 5], [7, 3], [3, 5]]
        expected = 10
        self.assertEqual(self.solution.maximumWealth(accounts), expected)

    def test_example_3(self):
        accounts = [[2, 8, 7], [7, 1, 3], [1, 9, 5]]
        expected = 17
        self.assertEqual(self.solution.maximumWealth(accounts), expected)

    def test_single_customer_single_account(self):
        accounts = [[5]]
        expected = 5
        self.assertEqual(self.solution.maximumWealth(accounts), expected)

    def test_multiple_customers_single_account(self):
        accounts = [[5], [10], [15]]
        expected = 15
        self.assertEqual(self.solution.maximumWealth(accounts), expected)

    def test_all_zero_accounts(self):
        accounts = [[0, 0], [0, 0]]
        expected = 0
        self.assertEqual(self.solution.maximumWealth(accounts), expected)

    def test_single_customer_multiple_accounts(self):
        accounts = [[1, 2, 3, 4, 5]]
        expected = 15
        self.assertEqual(self.solution.maximumWealth(accounts), expected)

    def test_two_customers_equal_wealth(self):
        accounts = [[2, 2, 2], [3, 3, 3]]
        expected = 9  # Both have equal wealth, but the richest is 9
        self.assertEqual(self.solution.maximumWealth(accounts), expected)

    def test_large_values(self):
        accounts = [[100, 100], [100, 100], [100, 100]]
        expected = 200
        self.assertEqual(self.solution.maximumWealth(accounts), expected)

    def test_edge_case_with_maximum_constraints(self):
        accounts = [[100] * 50]  # 50 accounts with 100 each
        expected = 5000
        self.assertEqual(self.solution.maximumWealth(accounts), expected)

    def test_non_sorted_accounts(self):
        accounts = [[5, 10], [20, 15], [10, 30]]
        expected = 40
        self.assertEqual(self.solution.maximumWealth(accounts), expected)

if __name__ == '__main__':
    unittest.main()
