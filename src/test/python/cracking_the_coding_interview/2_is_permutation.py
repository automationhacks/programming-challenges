"""
Problem 1.2 Page 90
Check Permutation: Given two strings, write a method to decide if one is a permutation of the other.
"""

"""
Below algorithm runs in O(N log N)
"""


def build_char_count_mapping(string):
    char_map = {}
    for char in string:
        if char in char_map:
            char_map[char] += 1
        else:
            char_map[char] = 1
    return char_map


def is_permutation(first, second):
    mapping = build_char_count_mapping(first)

    for char in second:
        if char not in mapping:
            return False
        else:
            mapping[char] -= 1

    return sum(mapping.values()) == 0


def test_is_permutation():
    assert is_permutation('abbccd', 'abcbcd') is True


def test_is_not_a_permutation():
    assert is_permutation('abbccd', 'abcbc') is False
