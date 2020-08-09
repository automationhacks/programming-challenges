import unittest

"""
Problem statement

Write an efficient function that checks whether any permutation of an input string is a palindrome.

You can assume the input string only contains lowercase letters.

Examples:

- "civic" should return True
- "ivicc" should return True
- "civil" should return False
- "livci" should return False
"""

"""
Solution Walk through

Our approach is to check that each character appears an even number of times, 
allowing for only one character to appear an odd number of times (a middle character). 
This is enough to determine if a permutation of the input string is a palindrome.

We iterate through each character in the input string, keeping track of the characters 
we’ve seen an odd number of times using a set unpaired_characters.

As we iterate through the characters in the input string:

- If the character is not in unpaired_characters, we add it.
- If the character is already in unpaired_characters, we remove it.

Finally, we just need to check if less than two characters don’t have a pair. 
"""


# O(n)
def has_palindrome_permutation(the_string):
    unpaired_chars = set()

    for char in the_string:
        if char in unpaired_chars:
            unpaired_chars.remove(char)
        else:
            unpaired_chars.add(char)

    return len(unpaired_chars) <= 1


# Tests
class Test(unittest.TestCase):

    def test_permutation_with_odd_number_of_chars(self):
        result = has_palindrome_permutation('aabcbcd')
        self.assertTrue(result)

    def test_permutation_with_even_number_of_chars(self):
        result = has_palindrome_permutation('aabccbdd')
        self.assertTrue(result)

    def test_no_permutation_with_odd_number_of_chars(self):
        result = has_palindrome_permutation('aabcd')
        self.assertFalse(result)

    def test_no_permutation_with_even_number_of_chars(self):
        result = has_palindrome_permutation('aabbcd')
        self.assertFalse(result)

    def test_empty_string(self):
        result = has_palindrome_permutation('')
        self.assertTrue(result)

    def test_one_character_string(self):
        result = has_palindrome_permutation('a')
        self.assertTrue(result)
