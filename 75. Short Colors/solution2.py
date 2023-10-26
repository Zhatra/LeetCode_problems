import unittest
from typing import List

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        low, mid, high = 0, 0, len(nums) - 1
        while mid <= high:
            if nums[mid] == 0:
                nums[low], nums[mid] = nums[mid], nums[low]
                low += 1
                mid += 1
            elif nums[mid] == 1:
                mid += 1
            else:
                nums[mid], nums[high] = nums[high], nums[mid]
                high -= 1











class TestSortColors(unittest.TestCase):

    def setUp(self):
        self.solution = Solution()

    def test_case_1(self):
        arr = [2, 0, 2, 1, 1, 0]
        self.solution.sortColors(arr)
        self.assertEqual(arr, [0, 0, 1, 1, 2, 2])

    def test_case_2(self):
        arr = [2, 2, 1]
        self.solution.sortColors(arr)
        self.assertEqual(arr, [1, 2, 2])

    def test_case_3(self):
        arr = [0]
        self.solution.sortColors(arr)
        self.assertEqual(arr, [0])

    def test_case_4(self):
        arr = [1, 0]
        self.solution.sortColors(arr)
        self.assertEqual(arr, [0, 1])

if __name__ == "__main__":
    unittest.main()
