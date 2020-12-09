"""
Given a string s, find the length of the longest substring without repeating characters.

Example 1:

Input: s = "abcabcbb" Output: 3 Explanation: The answer is "abc", with the length of 3.

Example 2:

Input: s = "bbbbb" Output: 1 Explanation: The answer is "b", with the length of 1.

Example 3:

Input: s = "pwwkew" Output: 3 Explanation: The answer is "wke", with the length of 3. Notice that
the answer must be a substring, "pwke" is a subsequence and not a substring.

Example 4:

Input: s = "" Output: 0

Constraints:

    0 <= s.length <= 5 * 104
    s consists of English letters, digits, symbols and spaces.
"""


# class Solution:
#     # Approach 1: Brute force
#     # Get all possible substrings by enumerating the string with two loops
#     # Run every substring through an allUnique method which checks if it has
#     # duplicate chars using set
#     # Complexity:
#     # Time: O(n ^ 3)
#     #   Outer loop runs once for every ch
#     #   Inner loop runs for outer until end
#     #   allUnique func runs for the length of the substring
#     # Space: min(n, m)
#     #   n is the string and m is the substring, where upper bound is
#
#     def lengthOfLongestSubstring(self, string: str) -> int:
#         length = len(string)
#
#         if length == 0:
#             return 0
#
#         ans = 0
#
#         for start in range(0, length - 1):
#             for end in range(start + 1, length):
#                 is_unique = self.allUnique(string, start, end)
#                 if is_unique:
#                     ans = max(ans, end - start)
#
#         return ans
#
#     def allUnique(self, string, start, end):
#         unique_chars = set()
#
#         for char_index in range(start, end):
#             character = string[char_index]
#             if character in unique_chars:
#                 return False
#             else:
#                 unique_chars.add(character)
#
#         return True


class Solution:
    # Back to our problem. We use HashSet to store the characters in current window [i,j) j == i initially).
    # Then we slide the index j to the right. If it is not in the HashSet, we slide
    # j further. Doing so until s[j] is already in the HashSet. At this point, we found the maximum size
    # of substrings without duplicate characters start with index i. If we do this for all i, we get
    # our answer.

    # Time: O(2n) worst case aaaaaaaaaa, each char would be visited twice by start and end
    # Space: O(min(m, n)), need O(k) space for sliding window, k = size of set, k is upper
    # bounded by size of string n and size of  charset/alphabet m

    def lengthOfLongestSubstring(self, string: str) -> int:
        length = len(string)
        chars = set()
        ans, start, end = 0, 0, 0

        while start < length and end < length:
            end_char = string[end]
            if end_char not in chars:
                chars.add(end_char)
                end += 1
                ans = max(ans, end - start)
            # if char at end is already present in the set
            # remove char at the start and repeat for all chars in string
            else:
                beginning_char = string[start]
                chars.remove(beginning_char)
                start += 1

        return ans


def test_long_string_with_repeating_chars():
    assert Solution().lengthOfLongestSubstring('abcabcbb') == 3


def test_empty_string():
    assert Solution().lengthOfLongestSubstring('') == 0


def test_all_repeating_chars():
    assert Solution().lengthOfLongestSubstring('aaaaaa') == 1
