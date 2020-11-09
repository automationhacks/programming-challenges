import unittest

# Write a recursive function for generating all permutations of an input string. Return them as a set.
# Don't worry about time or space complexity—if we wanted efficiency we'd write an iterative version.
# To start, assume every character in the input string is unique.
# Your function can have loops—it just needs to also be recursive.


# Time complexity: 
def get_permutations(string):
    # Generate all permutations of the input string recursively

    # Base case: When string is just one char
    if len(string) <= 1:
        return {string}

    all_chars_except_last = string[:-1]
    last_char = string[-1]

    # recursive call to get all possible permutations of all chars except last
    permutations_of_all_chars_except_last = get_permutations(all_chars_except_last)

    # Put the last char in all possible positions of each of the above permutations
    permutations = set()
    for each_permutation in permutations_of_all_chars_except_last:
        for position in range(len(all_chars_except_last) + 1):
            # Add last char to each possible position and add it as a permutation
            permutation = each_permutation[:position] + last_char + each_permutation[position:]
            permutations.add(permutation)

    return permutations


# Tests
class Test(unittest.TestCase):

    def test_empty_string(self):
        actual = get_permutations('')
        expected = {''}
        self.assertEqual(actual, expected)

    def test_one_character_string(self):
        actual = get_permutations('a')
        expected = {'a'}
        self.assertEqual(actual, expected)

    def test_two_character_string(self):
        actual = get_permutations('ab')
        expected = {'ab', 'ba'}
        self.assertEqual(actual, expected)

    def test_three_character_string(self):
        actual = get_permutations('abc')
        expected = {'abc', 'acb', 'bac', 'bca', 'cab', 'cba'}
        self.assertEqual(actual, expected)


unittest.main(verbosity=2)
