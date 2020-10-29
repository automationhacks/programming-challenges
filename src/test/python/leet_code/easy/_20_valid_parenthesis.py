"""
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

    Open brackets must be closed by the same type of brackets.
    Open brackets must be closed in the correct order.

Example 1:

Input: s = "()"
Output: true

Example 2:

Input: s = "()[]{}"
Output: true

Example 3:

Input: s = "(]"
Output: false

Example 4:

Input: s = "([)]"
Output: false

Example 5:

Input: s = "{[]}"
Output: true

Constraints:

    1 <= s.length <= 104
    s consists of parentheses only '()[]{}'.
"""
import pytest

"""
Runtime: 24 ms, faster than 94.49% of Python3 online submissions for Valid Parentheses.
Memory Usage: 14.1 MB, less than 100.00% of Python3 online submissions for Valid Parentheses.
"""


class Solution:
    def isValid(self, string: str) -> bool:

        if not string:
            return False

        stack = []

        left = ['[', '{', '(']
        right = [']', '}', ')']
        mapping = dict(zip(right, left))

        for symbol in string:
            if symbol in left:
                stack.append(symbol)
            elif symbol in right:
                if stack:
                    popped = stack.pop()

                    # Check if the last popped symbol is not the opening complement
                    # of right symbol
                    if not popped == mapping[symbol]:
                        return False
                # If stack is empty and we get a right symbol then the string is
                # already unbalanced
                else:
                    return False

            else:
                raise ValueError("Invalid symbol in the string, supported ones are [], {}, ()")

        return not stack


def test_empty():
    assert Solution().isValid('') is False


def test_string_with_spaces():
    with pytest.raises(ValueError):
        Solution().isValid('  ')


def test_balanced_single_bracket():
    assert Solution().isValid('()') is True


def test_balanced_multiple():
    assert Solution().isValid('({[]})') is True


def test_non_balanced_multiple():
    assert Solution().isValid('}({[]})') is False


def test_non_balanced_no_opening_brackets():
    assert Solution().isValid('}])(') is False
