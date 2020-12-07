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

# Original attempt

"""
class Solution:
    def lengthOfLongestSubstring(self, string: str) -> int:
        if string == "":
            return 0
        
        max_len = 1 
        str_len = len(string)
        
        for index, char in enumerate(string):
           seen = set([char])
        
           for next_char_index in range(index + 1, str_len): # index error at end
                next_char = string[next_char_index]
                
                if next_char in seen:
                    length =  len(seen)
                    if length > max_len:
                        max_len = length
                    break
                else:
                    seen.add(next_char)
                    
                    if next_char_index == str_len - 1 and len(seen) > max_len:
                        max_len = len(seen)
                    
        return max_len
"""

class Solution:
    # Approach 1: Brute force
    # Get all possible substrings by enumerating the string with two loops
    # Run every substring through an allUnique method which checks if it has
    # duplicate chars using set
    # Complexity:
    # Time: O(n ^ 3)
    #   Outer loop runs once for every ch
    #   Inner loop runs for outer until end
    #   allUnique func runs for the length of the substring
    # Space: min(n, m)
    #   n is the string and m is the substring, where upper bound is

    def lengthOfLongestSubstring_BruteForce(self, string: str) -> int:
        length = len(string)

        if length == 0:
            return 0

        ans = 0

        for start in range(0, length - 1):
            for end in range(start + 1, length):
                is_unique = self.allUnique(string, start, end)
                if is_unique:
                    ans = max(ans, end - start)

        return ans

    def allUnique(self, string, i, j):
        unique_chars = set()

        for ch_idx in range(i, j):
            character = string[ch_idx]
            if character in unique_chars:
                return False
            else:
                unique_chars.add(character)

        return True


def test_long_string_with_repeating_chars():
    assert Solution().lengthOfLongestSubstring('abcabcbb') == 3


def test_empty_string():
    assert Solution().lengthOfLongestSubstring('') == 0


def test_all_repeating_chars():
    assert Solution().lengthOfLongestSubstring('aaaaaa') == 1
