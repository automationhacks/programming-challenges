"""
Problem # 53
https://leetcode.com/problems/maximum-subarray/

Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

Follow up: If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle.

Example 1:

Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.

Example 2:

Input: nums = [1]
Output: 1

Example 3:

Input: nums = [0]
Output: 0

Example 4:

Input: nums = [-1]
Output: -1

Example 5:

Input: nums = [-2147483647]
Output: -2147483647



Constraints:

    1 <= nums.length <= 2 * 104
    -2^31 <= nums[i] <= 2^31 - 1
"""
from typing import List


class Solution:
    # Greedy approach to keep track of local sum and compare with global sum for every
    # number in the list

    # Time: O(n) since its a one pass algo
    # Space: O(1) since we keep couple of variables to store current and max sum
    def maxSubArray(self, nums: List[int]) -> int:
        nums_length = len(nums)
        curr_sum = max_sum = nums[0]

        for i in range(1, nums_length):
            curr_sum = max(nums[i], curr_sum + nums[i])
            max_sum = max(max_sum, curr_sum)

        return max_sum


def test_one_number():
    assert Solution().maxSubArray([1]) == 1


def test_small_array():
    assert Solution().maxSubArray([-2, 1, -3, 4]) == 4


def test_large_array():
    assert Solution().maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]) == 6
