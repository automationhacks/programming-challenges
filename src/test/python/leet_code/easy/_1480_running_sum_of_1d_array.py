"""
Source: Leetcode
Difficulty: Easy
Link: https://leetcode.com/problems/running-sum-of-1d-array/
Topic: Array

Given an array nums. We define a running sum of an array as runningSum[i] = sum(nums[0]…nums[i]).

Return the running sum of nums.

```
Example 1:

Input: nums = [1,2,3,4]
Output: [1,3,6,10]
Explanation: Running sum is obtained as follows: [1, 1+2, 1+2+3, 1+2+3+4].

Example 2:

Input: nums = [1,1,1,1,1]
Output: [1,2,3,4,5]
Explanation: Running sum is obtained as follows: [1, 1+1, 1+1+1, 1+1+1+1, 1+1+1+1+1].

Example 3:

Input: nums = [3,1,2,10,1]
Output: [3,4,6,16,17]
```

Constraints:

- 1 <= nums.length <= 1000
- -10^6 <= nums[i] <= 10^6

"""
from typing import List


class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        sum_so_far = 0
        result = []

        for num in nums:
            sum_so_far += num
            result.append(sum_so_far)

        return result


def test_running_sum_normal_number():
    # Normal input
    assert Solution().runningSum([1, 2, 3, 4]) == [1, 3, 6, 10]


def test_running_sum_same_numbers():
    assert Solution().runningSum([1, 1, 1, 1, 1]) == [1, 2, 3, 4, 5]


def test_running_num_single_item():
    assert Solution().runningSum([1]) == [1]


def test_running_sum_empty_list():
    assert Solution().runningSum([]) == []
