"""
Given a sorted array of distinct integers and a target value, return the index if the target is
found. If not, return the index where it would be if it were inserted in order.

Example 1:

Input: nums = [1,3,5,6], target = 5 Output: 2

Example 2:

Input: nums = [1,3,5,6], target = 2 Output: 1

Example 3:

Input: nums = [1,3,5,6], target = 7 Output: 4

Example 4:

Input: nums = [1,3,5,6], target = 0 Output: 0

Example 5:

Input: nums = [1], target = 0 Output: 0

Constraints:

    1 <= nums.length <= 104
    -104 <= nums[i] <= 104
    nums contains distinct values sorted in ascending order.
    -104 <= target <= 104
"""

# Approach: Use binary search on sorted array
# Time O(log n)
# Space: O(1)
from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1

        while left <= right:
            pivot = (left + right) // 2

            if nums[pivot] == target:
                return pivot
            if target < nums[pivot]:
                right = pivot - 1
            else:
                left = pivot + 1

        return left


def test_target_found():
    assert Solution().searchInsert([1, 3, 5, 6], 5) == 2


def test_target_not_found():
    assert Solution().searchInsert([1, 3, 5, 6], 2) == 1


def test_target_not_found_insert_at_end():
    assert Solution().searchInsert([1, 3, 5, 6], 7) == 4


def test_nums_with_one_item():
    assert Solution().searchInsert([1], 2) == 1
