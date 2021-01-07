"""
Source: Leetcode
Difficulty: Easy
Link: https://leetcode.com/problems/add-binary/
Topic: Math, String

Given two binary strings a and b, return their sum as a binary string.

Example 1:

Input: a = "11", b = "1" Output: "100"

Example 2:

Input: a = "1010", b = "1011" Output: "10101"

Constraints:

- 1 <= a.length, b.length <= 104
- a and b consist only of '0' or '1' characters.
- Each string does not contain leading zeros except for the zero itself.
"""


class Solution:
    # Time: O(max(n, m)) where n and m are length of first, second
    # Space: Same as above to keep the answer
    def addBinary(self, first: str, second: str) -> str:
        max_length = max(len(first), len(second))
        # Here zfill would pad the string on the left with required chars,
        # in this case zeroes
        first, second = first.zfill(max_length), second.zfill(max_length)

        carry = 0
        ans = []

        for index in range(max_length - 1, -1, -1):
            # Check if current index nos are 1 and if yes add to carry
            if first[index] == '1':
                carry += 1

            if second[index] == '1':
                carry += 1

            # Check modulo by 2 and if carry is 1 + 1, then add 1 to ans
            if carry % 2 == 1:
                ans.append('1')
            else:
                ans.append('0')

            # reset the carry
            carry //= 2

        # If there is still a carry left, add to answer
        if carry == 1:
            ans.append('1')

        # Reverse the list
        ans.reverse()

        # Return result binary added string
        return ''.join(ans)


def test_small():
    assert Solution().addBinary(first="11", second="1") == "100"


def test_medium():
    assert Solution().addBinary(first="1010", second="1011") == "10101"
