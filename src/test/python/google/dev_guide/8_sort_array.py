"""
Return an array that contains the sorted values from the input array with duplicates removed.

sort([]) → []
sort([1]) → [1]
sort([1, 1]) → [1]
sort([1, 2, 10, 9, 9, 7, 8, 5]) → [1, 2, 5, 7, 8, 9, 10]
"""

from collections import OrderedDict


def sort_with_dup_removed(arr):
    if len(arr) <= 1:
        return arr

    dct = OrderedDict()
    for num in arr:
        if num not in dct:
            dct[num] = 0

    arr_with_dup_removed = list(dct.keys())
    arr_with_dup_removed.sort()
    return arr_with_dup_removed


def test_sort_with_less_than_1_item():
    assert sort_with_dup_removed([1]) == [1]


def test_sort_with_multiple_duplicates():
    assert sort_with_dup_removed([1, 2, 10, 9, 9, 7, 8, 5]) == [1, 2, 5, 7, 8, 9, 10]
