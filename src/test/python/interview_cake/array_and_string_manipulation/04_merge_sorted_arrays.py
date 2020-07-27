"""
 In order to win the prize for most cookies sold, my friend Alice and I are going to merge our Girl Scout Cookies
 orders and enter as one unit.

Each order is represented by an "order id" (an integer).

We have our lists of orders sorted numerically already, in lists.
Write a function to merge our lists of orders into one sorted list.

For example:

my_list     = [3, 4, 6, 10, 11, 15]
alices_list = [1, 5, 8, 12, 14, 19]

# Prints [1, 3, 4, 5, 6, 8, 10, 11, 12, 14, 15, 19]
print(merge_lists(my_list, alices_list))
"""

import unittest


# O(n) time and space
def merge_lists(my_list, alices_list):
    # Take care of edge cases
    if not my_list and not alices_list:
        return []
    elif not my_list:
        return alices_list
    elif not alices_list:
        return my_list

    # Combine the sorted lists into one large sorted list
    merged = []

    larger, smaller = get_larger_smaller_list(alices_list, my_list)

    larger_ptr, smaller_ptr = 0, 0

    while larger_ptr < len(larger):
        if smaller_ptr < len(smaller):
            first = larger[larger_ptr]
            second = smaller[smaller_ptr]

            if first < second:
                merged.append(first)
                larger_ptr += 1
            else:
                merged.append(second)
                smaller_ptr += 1
        else:
            merged.append(larger[larger_ptr])
            larger_ptr += 1

    return merged


def get_larger_smaller_list(alices_list, my_list):
    my_list_length = len(my_list)
    alices_list_length = len(alices_list)

    if my_list_length > alices_list_length:
        return my_list, alices_list
    else:
        return alices_list, my_list


class Test(unittest.TestCase):

    def test_both_lists_are_empty(self):
        actual = merge_lists([], [])
        expected = []
        self.assertEqual(actual, expected)

    def test_first_list_is_empty(self):
        actual = merge_lists([], [1, 2, 3])
        expected = [1, 2, 3]
        self.assertEqual(actual, expected)

    def test_second_list_is_empty(self):
        actual = merge_lists([5, 6, 7], [])
        expected = [5, 6, 7]
        self.assertEqual(actual, expected)

    def test_both_lists_have_some_numbers(self):
        actual = merge_lists([2, 4, 6], [1, 3, 7])
        expected = [1, 2, 3, 4, 6, 7]
        self.assertEqual(actual, expected)

    def test_lists_are_different_lengths(self):
        actual = merge_lists([2, 4, 6, 8], [1, 7])
        expected = [1, 2, 4, 6, 7, 8]
        self.assertEqual(actual, expected)
