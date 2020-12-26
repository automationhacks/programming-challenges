"""
Source: Leetcode
Difficulty: Easy
Link: https://leetcode.com/problems/squares-of-a-sorted-array/
Topic: Arrays, Two pointer

Given an integer array nums sorted in non-decreasing order, return an array of the squares of each
number sorted in non-decreasing order.

Example 1:

```
Input: nums = [-4,-1,0,3,10]
Output: [0,1,9,16,100]
Explanation: After squaring, the array becomes [16,1,0,9,100].
After sorting, it becomes [0,1,9,16,100].
```

Example 2:

```
Input: nums = [-7,-3,2,3,11]
Output: [4,9,9,49,121]
```

Constraints:

- 1 <= nums.length <= 104
- -104 <= nums[i] <= 104
- nums is sorted in non-decreasing order.
"""


from typing import List

# Time: O(n)
# Space: O(n)
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        ans = []
        right = 0

        # Find the first positive no
        while right < len(nums) and nums[right] < 0:
            right += 1
        left = right - 1

        # Start two pointers
        # left in decreasing order and right in increasing order
        # compare the two nums and append the required one

        while 0 <= left and right < len(nums):
            left_squared = nums[left] ** 2
            right_squared = nums[right] ** 2

            if left_squared < right_squared:
                ans.append(left_squared)
                left -= 1
            else:
                ans.append(right_squared)
                right += 1

        # If left still has some items on the edge
        while left >= 0:
            ans.append(nums[left] ** 2)
            left -= 1

        # If right still has some items on the edge
        while right < len(nums):
            ans.append(nums[right] ** 2)
            right += 1

        return ans


def test_both_positive_and_negative():
    assert Solution().sortedSquares([-4, -1, 0, 3, 10]) == [0, 1, 9, 16, 100]
    assert Solution().sortedSquares([-7, -3, 2, 3, 11]) == [4, 9, 9, 49, 121]


def test_only_negative():
    assert Solution().sortedSquares([-5, -3, -2, -1]) == [1, 4, 9, 25]


def test_single_negative():
    assert Solution().sortedSquares([-5]) == [25]


def test_empty():
    assert Solution().sortedSquares([]) == []
