"""
Page 90:
Is Unique: Implement an algorithm to determine if a string has all unique characters. What if you cannot use additional data structures?
"""


# O(n / 2)
def does_string_have_dups(string):
    unique = set()
    for char in string:
        if char not in unique:
            unique.add(char)
        else:
            return False
    return True


# O(n log n)
def does_string_have_dups_without_extra_ds(string):
    sorted_str = sorted(string)
    end = len(string) - 1

    last_seen = ''
    while end > 0:
        ch = sorted_str[end]
        if last_seen == ch:
            return False
        else:
            last_seen = ch
        end -= 1
    return True


def test_string_without_unique_chars():
    assert does_string_have_dups('abdcbabbdcbddb') is False
    assert does_string_have_dups_without_extra_ds('abdcbabbdcbddb') is False


def test_string_with_all_unique_chars():
    assert does_string_have_dups('word') is True
    assert does_string_have_dups_without_extra_ds('word') is True
