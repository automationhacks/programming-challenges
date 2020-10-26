from typing import List

"""
Problem name: Two sum

Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Output: Because nums[0] + nums[1] == 9, we return [0, 1].

Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]

Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]

Constraints:

    2 <= nums.length <= 105
    -109 <= nums[i] <= 109
    -109 <= target <= 109
    Only one valid answer exists.
"""

"""
Complexity:
Since this is a one pass operation and lookup of keys in a dict is O(1), We
have time: O(n) and space O(n)
"""

"""
Runtime: 44 ms, faster than 91.82% of Python3 online submissions for Two Sum.
    Memory Usage: 15.5 MB, less than 16.53% of Python3 online submissions for Two Sum.
"""


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_to_index = {}

        # Iterate in list one item at a time
        for index, num in enumerate(nums):
            # Figure out the complement that we should find in the list
            complement = target - num
            # Use a dict to reduce the look up of number to value to O(1)
            # See if the complement already exists in the dict and exit early
            # if found
            if complement in nums_to_index:
                # We use sorted() before return to ensure the index are always ordered since we could find complement
                # in an earlier no. Since the return list would always have len = 2, we can disregard this as O(1)
                # and not add into time complexity
                return sorted([index, nums_to_index[complement]])

            nums_to_index[num] = index

        return []


def test_short_list():
    solution = Solution()
    assert solution.twoSum(nums=[2, 6, 4], target=6) == [0, 2]


def test_long_list():
    solution = Solution()
    assert solution.twoSum(nums=[2, 7, 11, 15], target=9) == [0, 1]


def test_duplicate():
    solution = Solution()
    assert solution.twoSum(nums=[3, 3], target=6) == [0, 1]


def test_no_complement_exists():
    solution = Solution()
    assert solution.twoSum(nums=[2, 3, 5], target=10) == []
