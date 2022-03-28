import unittest
from max_subsequence_sum import max_subsequence_sum


class TestMaxSubSequenceSum(unittest.TestCase):
    def testcase(self):
        self.assertEqual(max_subsequence_sum([5]), 5)
        self.assertEqual(max_subsequence_sum((-5, 3, -5, 1, -1)), 3)
        self.assertEqual(max_subsequence_sum((3, -3, 5, -2, 4, -1, -2, 5, -2)), 9)
        

if __name__ == '__main__':
    unittest.main()