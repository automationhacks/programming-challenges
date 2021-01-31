"""
Source: Leetcode
Difficulty: Easy
Link: https://leetcode.com/problems/defanging-an-ip-address/
Topic: String

Given a valid (IPv4) IP address, return a defanged version of that IP address.

A defanged IP address replaces every period "." with "[.]".

Example 1:

Input: address = "1.1.1.1"
Output: "1[.]1[.]1[.]1"

Example 2:

Input: address = "255.100.50.0"
Output: "255[.]100[.]50[.]0"

Constraints:

    The given address is a valid IPv4 address.
"""

"""
Approach:

Iterate in IP address and keep on adding digits, until you come across ., wherein you add the defanged symbol

Complexity:
Time: O(n)
Space: O(1), since size of IPV4 is always constant, we would need a constant space
"""


class Solution:
    def defangIPaddr(self, address: str) -> str:
        defangled = ''

        for char in address:
            if char != '.':
                defangled += char
            else:
                defangled += '[.]'

        return defangled


def test_ip_address_is_defanged_low_range():
    assert Solution().defangIPaddr('1.1.1.1') == '1[.]1[.]1[.]1'


def test_ip_address_is_defanged_high_range():
    assert Solution().defangIPaddr('255.255.255.255') == '255[.]255[.]255[.]255'
