"""
Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

Symbol Value I 1 V 5 X 10 L 50 C 100 D 500 M 1000

For example, 2 is written as II in Roman numeral, just two one's added together. 12 is written as
XII, which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.

Roman numerals are usually written largest to smallest from left to right. However, the numeral for
four is not IIII. Instead, the number four is written as IV. Because the one is before the five we
subtract it making four. The same principle applies to the number nine, which is written as IX.
There are six instances where subtraction is used:

    I can be placed before V (5) and X (10) to make 4 and 9.
    X can be placed before L (50) and C (100) to make 40 and 90.
    C can be placed before D (500) and M (1000) to make 400 and 900.

Given a roman numeral, convert it to an integer.

Example 1:

Input: s = "III" Output: 3

Example 2:

Input: s = "IV" Output: 4

Example 3:

Input: s = "IX" Output: 9

Example 4:

Input: s = "LVIII" Output: 58 Explanation: L = 50, V= 5, III = 3.

Example 5:

Input: s = "MCMXCIV" Output: 1994 Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.

Constraints:

    1 <= s.length <= 15
    s contains only the characters ('I', 'V', 'X', 'L', 'C', 'D', 'M').
    It is guaranteed that s is a valid roman numeral in the range [1, 3999].
"""

"""
Runtime: 40 ms, faster than 91.61% of Python3 online submissions for Roman to Integer.
Memory Usage: 14.1 MB, less than 100.00% of Python3 online submissions for Roman to Integer.
"""

class Solution:
    def romanToInt(self, roman_no: str) -> int:

        # Approach:
        # Complexity analysis: Time: O(n) and space O(1)
        # create a mapping of roman to int values
        # create a mapping of roman symbols to next symbols which can cause substraction
        # parse the roman str one char at a time and get the value and add to a final value
        # Check if next symbol satisfies substraction rules and then do next - current value and skip 2 symbols
        # return the final value

        roman_no_len = len(roman_no)
        roman_to_integer = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

        subtraction_rules = {
            'I': ['V', 'X'],
            'X': ['L', 'C'],
            'C': ['D', 'M']
        }

        result = 0
        index = 0

        while index < roman_no_len:
            current_symbol = roman_no[index]
            current_symbol_value = roman_to_integer[current_symbol]

            # Edge condition: If we are the last digit in the no
            if index == roman_no_len - 1:
                result += current_symbol_value
                return result

            # Check if current and next symbol satisfies substraction rules
            next_symbol = roman_no[index + 1]

            if current_symbol in subtraction_rules.keys() and next_symbol in subtraction_rules[current_symbol]:
                next_symbol_value = roman_to_integer[next_symbol]
                result += next_symbol_value - current_symbol_value
                index += 2
            else:
                result += roman_to_integer[current_symbol]
                index += 1

        return result


def test_only_ones():
    assert Solution().romanToInt('III') == 3


def test_only_non_ones():
    assert Solution().romanToInt('VXDMIII') == 1518


def test_substraction_rules():
    assert Solution().romanToInt('MCMXCIV') == 1994
