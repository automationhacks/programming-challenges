"""
CTCI 6th edition: Chapter 1: Arrays and Strings, Problem 1.9

String Rotation: Assume you have a method isSubstring which checks if one word is a substring of another.
Given two strings, s1 and s2, write code to check if s2 is a rotation of s1 using
only one call to isSubstring (e.g.,"waterbottle"is a rotation of"erbottlewat").
Hints: #34, #88, #104

- If a string is a rotation of another, then it's a rotation at a particular point.
For example, a rotation of waterbottle at character 3 means cutting waterbottle at character 3 and putting
the right half (erbottle) before the left half (wat).

We are essentially asking if there's a way of splitting the first string into two parts, x and y,
such that first string is xy and second is yx.For example,x =wat and y = erbottle.
The first string is xy = waterbottle.The second string is yx = erbottlewat.

Think about the earlier hint. Then think about what happens when you concatenate erbottlewat to itself.
You get erbottlewaterbottlewat.

https://github.com/careercup/CtCI-6th-Edition-Python/blob/master/Chapter1/9_String%20Rotation/StringRotation.py
"""


# O(N)
def is_substring(string, sub):
    return string.find(sub) != -1


def is_string_rotation(first, second):
    if len(first) == len(second):
        return is_substring(first + first, second)
    return False


def test_is_string_rotation():
    data = [
        ('waterbottle', 'erbottlewat', True),
        ('foo', 'bar', False),
        ('foo', 'foofoo', False)
    ]
    for first, second, expected in data:
        assert is_string_rotation(first, second) == expected
