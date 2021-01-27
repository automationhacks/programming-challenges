"""
Source: Leetcode
Difficulty: Easy
Link: https://leetcode.com/problems/remove-vowels-from-a-string/
Topic: String

Given a string s, remove the vowels 'a', 'e', 'i', 'o', and 'u' from it,
and return the new string.

Example 1:

Input: s = "leetcodeisacommunityforcoders"
Output: "ltcdscmmntyfrcdrs"

Example 2:

Input: s = "aeiou"
Output: ""
"""


class Solution:
    """
    Approach:
    Walk through the string,
    check if char is in vowels,
    and if not then add it to the result string

    Time: O(n)
    Space: O(n)
    """

    def removeVowels(self, string: str) -> str:
        vowels = 'aeiou'

        without_vowels = []
        for char in string:
            if char not in vowels:
                without_vowels.append(char)

        return ''.join(without_vowels)


def test_remove_vowels_in_string():
    assert Solution().removeVowels('leetcodeisacommunityforcoders') == 'ltcdscmmntyfrcdrs'


def test_remove_only_vowels_in_string():
    assert Solution().removeVowels('aeiou') == ''
