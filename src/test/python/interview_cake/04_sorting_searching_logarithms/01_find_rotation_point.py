"""
I want to learn some big words so people think I'm smart.

I opened up a dictionary to a page in the middle and started flipping through, looking for words I
didn't know. I put each word I didn't know at increasing indices in a huge list I created in memory.
When I reached the end of the dictionary, I started from the beginning and did the same thing until
I reached the page I started at.

Now I have a list of words that are mostly alphabetical, except they start somewhere in the middle
of the alphabet, reach the end, and then start from the beginning of the alphabet. In other words,
this is an alphabetically ordered list that has been "rotated." For example:

words = [
    'ptolemaic',
    'retrograde',
    'supplant',
    'undulate',
    'xenoepist',
    'asymptote',  # <-- rotates here!
    'babka',
    'banoffee',
    'engender',
    'karpatka',
    'othellolagkage',
]


Write a function for finding the index of the "rotation point," which is where I started working
from the beginning of the dictionary. This list is huge (there are lots of words I don't know) so we
want to be efficient here.
"""

import unittest


# O(log n) time and O(1) space
def find_rotation_point(words):
    first_word = words[0]

    # Handle case of if list is not rotated
    if first_word[0] == 'a':
        return 0

    floor = -1
    ceiling = len(words)

    while floor + 1 < ceiling:
        distance = ceiling - floor
        half_distance = distance // 2
        guess_index = floor + half_distance

        current_word = words[guess_index]

        # words = ['k', 'v', 'a', 'b', 'c', 'd', 'e', 'g', 'i']
        # If we are at 'c' then since 'c' is less than 'k'
        # then we know the rotation point would be to the left (move ceiling)
        # words = ['b', 'c', 'd', 'e', 'g', 'i', 'k', 'v', 'a', ]
        # but if we were at 'k', then we know rotation point would be to the right (move floor)
        if current_word >= first_word:
            floor = guess_index
        else:
            ceiling = guess_index

        # if floor and ceiling have converged
        if floor + 1 == ceiling:
            # Between floor and ceiling is where we flipped to the beginning
            # so ceiling is alphabetically first
            return ceiling

    return -1


class Test(unittest.TestCase):

    def test_small_list(self):
        actual = find_rotation_point(['cape', 'cake'])
        expected = 1
        self.assertEqual(actual, expected)

    def test_non_rotated_list(self):
        actual = find_rotation_point(['apple', 'ask', 'ball', 'cat'])
        expected = 0
        self.assertEqual(actual, expected)

    def test_medium_list(self):
        actual = find_rotation_point(['grape', 'orange', 'plum',
                                      'radish', 'apple'])
        expected = 4
        self.assertEqual(actual, expected)

    def test_large_list(self):
        actual = find_rotation_point(['ptolemaic', 'retrograde', 'supplant',
                                      'undulate', 'xenoepist', 'asymptote',
                                      'babka', 'banoffee', 'engender',
                                      'karpatka', 'othellolagkage'])
        expected = 5
        self.assertEqual(actual, expected)
