"""
Determine whether an integer is a palindrome. An integer is a palindrome when it reads the same backward as forward.

Follow up: Could you solve it without converting the integer to a string?

Example 1:

Input: x = 121
Output: true

Example 2:

Input: x = -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.

Example 3:

Input: x = 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.

Example 4:

Input: x = -101
Output: false

Constraints:

    -2 ^ 31 <= x <= 2 ^ 31 - 1
"""


class Solution:
    def isPalindrome(self, num: int) -> bool:
        return self.is_palindrome_without_str_conversion(num)

    # Time: O(n) and Space: O(n)
    # Convert to str and start two pointers from left and right
    # comparing the chars
    def is_palindrome_using_str_convertion(self, num):

        num_str = str(num)
        left, right = 0, len(num_str) - 1

        while left < right:
            if num_str[left] != num_str[right]:
                return False

            left += 1
            right -= 1

        return True

    # Follow up
    # Reverse the integer and then compare with original
    # Time: O(n) and Space: O(1)
    def is_palindrome_without_str_conversion(self, num):
        original_num = num

        # If no (-121) is negative then after reversal it would be (121-)
        # which are not equal and hence not a palindrome
        if original_num < 0:
            return False

        reversed_num = 0
        min_range = -2 ** 31
        max_range = 2 ** 31 - 1

        while num != 0:
            remainder = num % 10
            temp = reversed_num * 10 + remainder

            # Takes care of integer overflow case
            # Note: In python the no never overflows, since as soon as it does
            # A larger space is allocated. This is to just demo how the case would be
            # for other languages
            if temp not in range(min_range, max_range):
                return False

            reversed_num = temp
            num = num // 10

        return original_num == reversed_num


def test_zero():
    assert Solution().is_palindrome_without_str_conversion(0) is True


def test_single_digit():
    assert Solution().is_palindrome_without_str_conversion(1) is True


def test_positive_palindrome_no():
    assert Solution().is_palindrome_without_str_conversion(121) is True


def test_positive_non_palindrome_no():
    assert Solution().is_palindrome_without_str_conversion(1234) is False


def test_negative_palindrome_no():
    assert Solution().is_palindrome_without_str_conversion(-121) is False


def test_negative_non_palindrome_no():
    assert Solution().is_palindrome_without_str_conversion(-1234) is False


def test_non_palindrome_no_overflow():
    assert Solution().is_palindrome_without_str_conversion(2 ** 32) is False
