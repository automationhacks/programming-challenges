"""
Source: Leetcode
Difficulty: Easy
Link: https://leetcode.com/problems/make-two-arrays-equal-by-reversing-sub-arrays/
Topic: Arrays

Given two integer arrays of equal length target and arr.

In one step, you can select any non-empty sub-array of arr and reverse it. You are allowed to make
any number of steps.

Return True if you can make arr equal to target, or False otherwise.

```
Example 1:

Input: target = [1,2,3,4], arr = [2,4,1,3]
Output: true
Explanation: You can follow the next steps to convert arr to target:
1- Reverse sub-array [2,4,1], arr becomes [1,4,2,3]
2- Reverse sub-array [4,2], arr becomes [1,2,4,3]
3- Reverse sub-array [4,3], arr becomes [1,2,3,4]
There are multiple ways to convert arr to target, this is not the only way to do so.

Example 2:

Input: target = [7], arr = [7]
Output: true
Explanation: arr is equal to target without any reverses.

Example 3:

Input: target = [1,12], arr = [12,1]
Output: true

Example 4:

Input: target = [3,7,9], arr = [3,7,11]
Output: false
Explanation: arr doesn't have value 9 and it can never be converted to target.

Example 5:

Input: target = [1,1,1,1,1], arr = [1,1,1,1,1]
Output: true
```

Constraints:

- target.length == arr.length
- 1 <= target.length <= 1000
- 1 <= target[i] <= 1000
- 1 <= arr[i] <= 1000
"""
from collections import Counter
from typing import List


class Solution:
    # Use a counter to get count of each no in the target and input arr
    # Compare if these two match.
    # Time: O(n + m + n) where n is len of target arr and m is length of input array
    # Space: O(n + m) for the counter dictionary
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        arr_counter = Counter(arr)
        target_counter = Counter(target)

        for no, count in target_counter.items():
            if no in arr_counter and count == arr_counter[no]:
                continue
            else:
                return False

        return True

    # Another approach could be to sort both the arrays and compare
    # Time: O(n + n log(n)) =>  nlog(n) for sorting and O(n) time for comparison thus, O(nlog(n))
    # Space: O(1), won't need additional space since sort the arrays in place using .sort()
    # def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
    #     target.sort()
    #     arr.sort()
    #
    #     return target == arr


def test_arrays_can_be_equal():
    target = [1, 2, 3, 4]
    arr = [2, 4, 1, 3]
    assert Solution().canBeEqual(target, arr) is True


def test_arrays_cannot_be_equal():
    target = [1, 2, 3, 4, 5]
    arr = [2, 4, 1, 3]
    assert Solution().canBeEqual(target, arr) is False
