"""
Source: Leetcode
Difficulty: Easy
Link: https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/
Topic: Array

Given an array of integers where 1 ≤ a[i] ≤ n (n = size of array), some elements appear twice and others appear once.

Find all the elements of [1, n] inclusive that do not appear in this array.

Could you do it without extra space and in O(n) runtime? You may assume the returned list does not count as extra space.

Example:

Input:
[4,3,2,7,8,2,3,1]

Output:
[5,6]
"""
from typing import List


class Solution:

    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        """
        Approach:

        - Convert the list to a set
        - Iterate from 1 .. len(nums) and check if the no is not in the set and add it to the result O(n)

        Time: O(n)
        Space: O(n)
        """
        unique_nums = set()
        max_range = len(nums)

        for num in nums:
            unique_nums.add(num)

        ans = []
        for num in range(1, max_range + 1):
            if num not in unique_nums:
                ans.append(num)

        return ans

    def findDisappearedNumbersOptimized(self, nums: List[int]) -> List[int]:
        """
        More mem efficient algo compared to above, Since we know the array has nums between 1 to n (size of the array)
        We mark nums which are already seen as negative, to avoid changing the value in one pass
        We then iterate from 1 to n and return the nums which are not negative (i.e. not seen ever)

        Time: O(n)
        Space: O(1)
        """
        for i in range(len(nums)):
            new_index = abs(nums[i]) - 1

            # Mark the num at nums[i] as visited
            if nums[new_index] > 0:
                nums[new_index] *= -1

        result = []
        for i in range(1, len(nums) + 1):
            if nums[i - 1] > 0:
                result.append(i)

        return result


def test_disappeared_nums():
    assert Solution().findDisappearedNumbersOptimized([4, 3, 2, 7, 8, 2, 3, 1]) == [5, 6]


def test_disappeared_nums_with_low_range():
    assert Solution().findDisappearedNumbersOptimized([1, 1]) == [2]
