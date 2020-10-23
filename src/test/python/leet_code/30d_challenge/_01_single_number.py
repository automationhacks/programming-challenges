"""
Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.

Follow up: Could you implement a solution with a linear runtime complexity and without using extra memory?



Example 1:

Input: nums = [2,2,1]
Output: 1

Example 2:

Input: nums = [4,1,2,1,2]
Output: 4

Example 3:

Input: nums = [1]
Output: 1



Constraints:

    1 <= nums.length <= 3 * 104
    -3 * 104 <= nums[i] <= 3 * 104
    Each element in the array appears twice except for one element which appears only once.


"""
from collections import defaultdict
from typing import List


# Approach 1: Use dict to keep track of count
#
def single_number(nums: List[int]) -> int:
    seen = defaultdict(int)

    for num in nums:
        seen[num] += 1

    for number, count in seen.items():
        if count == 1:
            return number


def test_single_no():
    assert single_number([1]) == 1


def test_small_list():
    assert single_number([2, 2, 1]) == 1


def test_long_list():
    assert single_number([4, 1, 2, 1, 2]) == 4
