"""
Given three integer arrays arr1, arr2 and arr3 sorted in strictly increasing order, return a sorted
array of only the integers that appeared in all three arrays.

Example 1:

Input: arr1 = [1,2,3,4,5], arr2 = [1,2,5,7,9], arr3 = [1,3,4,5,8] Output: [1,5] Explanation: Only 1
and 5 appeared in the three arrays.

Constraints:

    1 <= arr1.length, arr2.length, arr3.length <= 1000
    1 <= arr1[i], arr2[i], arr3[i] <= 2000
"""
import collections

from typing import List


class Solution:
    # Approach 1: Use a hash map with counts of each number and add the ones that count exactly 3 times
    # Time O(n) where n is the length of all the array combined
    # Space O(n) where we use a hashmap to store the number and its count
    def arraysIntersectionX(self, arr1: List[int], arr2: List[int], arr3: List[int]) -> List[int]:
        ans = []

        counter = collections.Counter(arr1 + arr2 + arr3)

        for item in counter:
            if counter[item] == 3:
                ans.append(item)

        return ans

    # Approach 2: Use three pointers
    # Have three pointers and move them in the 3 arrays by comparing if the current pointer < second and always moving
    # the smaller pointer
    # Time: O(n)
    # Space: O(1) since we don't use any additional space
    def arraysIntersection(self, arr1: List[int], arr2: List[int], arr3: List[int]) -> List[int]:
        ans = []

        p1 = p2 = p3 = 0
        while p1 < len(arr1) and p2 < len(arr2) and p3 < len(arr3):
            if arr1[p1] == arr2[p2] == arr3[p3]:
                ans.append(arr1[p1])
                p1 += 1
                p2 += 1
                p3 += 1
            else:
                if arr1[p1] < arr2[p2]:
                    p1 += 1
                elif arr2[p2] < arr3[p3]:
                    p2 += 1
                # p3 must be less than p1 and p2
                else:
                    p3 += 1

        return ans


def test_intersection_happens():
    assert Solution().arraysIntersection(arr1=[1, 2, 3, 4, 5], arr2=[1, 2, 5, 7, 9], arr3=[1, 3, 4, 5, 8]) == [1, 5]


def test_intersection_does_not_happen():
    assert Solution().arraysIntersection(arr1=[2, 3, 5], arr2=[2, 4, 7, 9], arr3=[3, 4, 6, 8]) == []
