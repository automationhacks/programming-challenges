"""
28. Implement strStr() Easy

Implement strStr().

Return the index of the first occurrence of needle in haystack, or -1 if needle is not part of
haystack.

Clarification:

What should we return when needle is an empty string? This is a great question to ask during an
interview.

For the purpose of this problem, we will return 0 when needle is an empty string. This is consistent
to C's strstr() and Java's indexOf().

Example 1:

Input: haystack = "hello", needle = "ll" Output: 2

Example 2:

Input: haystack = "aaaaa", needle = "bba" Output: -1

Example 3:

Input: haystack = "", needle = "" Output: 0

Constraints:

    0 <= haystack.length, needle.length <= 5 * 104
    haystack and needle consist of only lower-case English characters.
"""


class Solution:

    # Approach 1: Substring: Linear time slice

    # Implement a sliding window wherein you compare the substring in window with needle
    # Complexity: O(N - L) * L where N is length of haystack and L is length of needle,
    # since we compute a substring of length L in a loop which is atmost executed (N - L) times
    # Space: O(1)

    # Problem with above is that we compare all substrings of length L with the needle
    # We can mitigate that, by only doing substring if the first character matches.

    # A more optimized approach which would make use of some math is to use Rabin karp pattern matching algorithm
    # Know more here: https://www.youtube.com/watch?v=qQ8vS2btsxI
    # That promises a runtime of O(NL) by selection of a strong hash function and also doing a rolling hash on the
    # string

    def strStr(self, haystack: str, needle: str) -> int:
        needle_len = len(needle)
        if needle_len == 0:
            return 0

        haystack_len = len(haystack)

        until = haystack_len - needle_len + 1
        for start in range(until):
            if haystack[start] == needle[0]:
                if haystack[start : start + needle_len] == needle:
                    return start

        return -1


def test_successful_match():
    assert Solution().strStr("hello", "ll") == 2

def test_unsuccessful_match():
    assert Solution().strStr("hello", "a") == -1

def test_empty_haystack():
    assert Solution().strStr("", "a") == -1

def test_empty_needle():
    assert Solution().strStr("a", "") == 0 