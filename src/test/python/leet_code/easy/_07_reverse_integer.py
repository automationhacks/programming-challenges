"""
Given a 32-bit signed integer, reverse digits of an integer.

Note: Assume we are dealing with an environment that could only store integers within the 32-bit
signed integer range: [−2 ^ 31, 2 ^ 31 − 1]. For the purpose of this problem, assume that your function
returns 0 when the reversed integer overflows.

Example 1:

Input: x = 123 Output: 321

Example 2:

Input: x = -123 Output: -321

Example 3:

Input: x = 120 Output: 21

Example 4:

Input: x = 0 Output: 0

"""

"""
Key learnings from this problem

- digit % 10 is not the same for 123 and -123, i.e. 123 % 10 = 3, -123 % 10 = 7
- You can construct reversed no using initial no * 10 + remainder
- You can check if a no lies between a range using range(start, end)
- Integers can be signed or unsigned and have a range of - 2 ^ 31 and  2 ^ 31 - 1,
  and 2 ^ 31 = 2,14,748,3648

"""


# Time O(n), Space O(1)
class Solution:
    def reverse(self, num):
        # Constraints
        min_range = -2 ** 31
        max_range = 2 ** 31 - 1

        # Figure out if no is negative, however operate on absolute value for reversal,
        # Else the results are wrong
        is_negative = num < 0
        num = abs(num)

        rev = 0
        while num != 0:
            # Core operation of getting last digit and
            # constructing the reversed no itself
            remainder = num % 10
            temp = rev * 10 + remainder

            # Check if no being reversed has overflowed
            if self.is_overflow(temp, min_range, max_range):
                return 0
            else:
                rev = temp

            num = num // 10

        # Return no with apt sign
        return -1 * rev if is_negative else rev

    @staticmethod
    def is_overflow(num, min_range, max_range):
        if num not in range(min_range, max_range):
            return True
        else:
            return False


# Test cases
def test_zero():
    solv = Solution()
    assert solv.reverse(0) == 0


def test_positive():
    solv = Solution()
    assert solv.reverse(123) == 321


def test_negative():
    solv = Solution()
    assert solv.reverse(-123) == -321


def test_trailing_zeroes():
    solv = Solution()
    assert solv.reverse(120) == 21


def test_large_no_causing_overflow():
    solv = Solution()
    assert solv.reverse(2147483648) == 0
