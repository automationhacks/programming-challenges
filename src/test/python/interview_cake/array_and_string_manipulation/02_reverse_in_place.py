"""
Source: https://www.interviewcake.com/question/python3/reverse-string-in-place?course=fc1&section=array-and-string-manipulation
Write a function that takes a list of characters and reverses the letters in place
"""

import unittest


# O(n) time and O(1) space
# Approach
# We swap first with last and do this till we reach the middle

def reverse(list_of_chars):
    beg = 0
    end = len(list_of_chars) - 1

    while beg <= end:
        list_of_chars[beg], list_of_chars[end] = list_of_chars[end], list_of_chars[beg]

        beg += 1
        end -= 1

    return list_of_chars


class Test(unittest.TestCase):

    def test_empty_string(self):
        list_of_chars = []
        reverse(list_of_chars)
        expected = []
        self.assertEqual(list_of_chars, expected)

    def test_single_character_string(self):
        list_of_chars = ['A']
        reverse(list_of_chars)
        expected = ['A']
        self.assertEqual(list_of_chars, expected)

    def test_longer_string(self):
        list_of_chars = ['A', 'B', 'C', 'D', 'E']
        reverse(list_of_chars)
        expected = ['E', 'D', 'C', 'B', 'A']
        self.assertEqual(list_of_chars, expected)
