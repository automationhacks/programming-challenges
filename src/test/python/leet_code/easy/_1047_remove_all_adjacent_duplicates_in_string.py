"""
Source: Leetcode
Difficulty: Easy
Link: https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string/
Topic: Stack

Given a string S of lowercase letters, a duplicate removal consists of choosing two adjacent and
equal letters, and removing them.

We repeatedly make duplicate removals on S until we no longer can.

Return the final string after all such duplicate removals have been made. It is guaranteed the
answer is unique.

Example 1:

Input: "abbaca" Output: "ca" Explanation: For example, in "abbaca" we could remove "bb" since the
letters are adjacent and equal, and this is the only possible move. The result of this move is that
the string is "aaca", of which only "aa" is possible, so the final string is "ca".

Note:

    1 <= S.length <= 20000
    S consists only of English lowercase letters.
"""


# Approach: Use a stack to evaluate the string greedily
# Time: O(n)
# Space: O(n - d) where d is the total length of all duplicates
class Solution:
    def removeDuplicates(self, string: str) -> str:
        stack = []

        for char in string:
            if stack and char == stack[-1]:
                stack.pop()
            else:
                stack.append(char)

        return ''.join(stack)


def test_remove_dups():
    assert Solution().removeDuplicates('abbaca') == 'ca'
