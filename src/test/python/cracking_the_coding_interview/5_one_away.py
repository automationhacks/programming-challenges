"""
Problem: One Away: There are three types of edits that can be performed on strings:
insert a character, remove a character, or replace a character.
Given two strings, write a function to check if they are one edit (or zero edits) away.

EXAMPLE
pale, pIe -> true
pales, pale -> true
pale, bale -> true
pale, bake -> false
"""


# Solution O(n)
# https://github.com/careercup/CtCI-6th-Edition-Python/blob/master/Chapter1/5_One%20Away/OneAway.py

# Hints
# - Start with the easy thing. Can you check each of the conditions separately?
# - What is the relationship between the "insert character" option and the "remove character" option?
# Do these need to be two separate checks?
# - Can you do all three checks in a single pass?

def one_away(first, second):
    length_diff_more_than_one = abs(len(first) - len(second)) > 1
    if length_diff_more_than_one:
        return False

    if len(first) == len(second):
        return one_edit_replace(first, second)
    elif len(first) + 1 == len(second):
        return one_edit_insert(first, second)
    elif len(first) - 1 == len(second):
        return one_edit_insert(second, first)
    return False


def one_edit_insert(first, second):
    edited = False
    i, j = 0, 0
    while i < len(first) and j < len(second):

        first_char = first[i]
        second_char = second[j]

        if first_char != second_char:
            if edited:
                return False
            edited = True
            j += 1
        else:
            i += 1
            j += 1
    return True


def one_edit_replace(first, second):
    edited = False
    for c1, c2 in zip(first, second):
        if c1 != c2:
            if edited:
                return False
            edited = True
    return True


def test_one_away():
    data = [
        ('pale', 'ple', True),
        ('pales', 'pale', True),
        ('pale', 'bake', False)
    ]

    for first, second, expected in data:
        assert one_away(first, second) is expected
