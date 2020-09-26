"""
Find a duplicate, Space Edition™.

We have a list of integers, where:

    The integers are in the range 1..n1..n1..n
    The list has a length of n+1n+1n+1

It follows that our list has at least one integer which appears at least twice. But it may have
several duplicates, and each duplicate may appear more than twice.

Write a function which finds an integer that appears more than once in our list. (If there are
multiple duplicates, you only need to find one of them.)

We're going to run this function on our new, super-hip MacBook Pro With Retina Display™. Thing is,
the damn thing came with the RAM soldered right to the motherboard, so we can't upgrade our RAM. So
we need to optimize for space!
"""

import unittest


def find_repeat(numbers):
    # Aproach 1: Use a set to remember previously seen numbers
    # time O(n) space O(n)
    # numbers_seen = set()

    # for number in numbers:
    #     if number in numbers_seen:
    #         return number
    #     else:
    #         numbers_seen.add(number)
    # return 0

    # Approach 2: Sort first (in-place) and then figure out if adjacent no is
    # repeated
    # time n log(n) space O(1)
    # numbers.sort()

    # for n in range(len(numbers) - 1, -1, -1):
    #     if numbers[n] == numbers[n - 1]:
    #         return numbers[n]
    # return 0

    # Approach 3: Use binary search to divide the list of possibilities
    floor = 1
    ceiling = len(numbers) - 1

    while floor < ceiling:
        # Divide our range 1..n into an upper range and lower range
        # (such that they don't overlap)
        # Lower range is floor..midpoint
        # Upper range is midpoint+1..ceiling
        midpoint = floor + ((ceiling - floor) // 2)
        lower_range_floor, lower_range_ceiling = floor, midpoint
        upper_range_floor, upper_range_ceiling = midpoint + 1, ceiling

        # Count number of items in lower range
        items_in_lower_range = 0
        for item in numbers:
            # Is it in the lower range?
            if item >= lower_range_floor and item <= lower_range_ceiling:
                items_in_lower_range += 1

        distinct_possible_integers_in_lower_range = (
                lower_range_ceiling
                - lower_range_floor
                + 1
        )
        if items_in_lower_range > distinct_possible_integers_in_lower_range:
            # There must be a duplicate in the lower range
            # so use the same approach iteratively on that range
            floor, ceiling = lower_range_floor, lower_range_ceiling
        else:
            # There must be a duplicate in the upper range
            # so use the same approach iteratively on that range
            floor, ceiling = upper_range_floor, upper_range_ceiling

    # Floor and ceiling have converged
    # We found a number that repeats!
    return floor


# Tests

class Test(unittest.TestCase):

    def test_just_the_repeated_number(self):
        actual = find_repeat([1, 1])
        expected = 1
        self.assertEqual(actual, expected)

    def test_short_list(self):
        actual = find_repeat([1, 2, 3, 2])
        expected = 2
        self.assertEqual(actual, expected)

    def test_medium_list(self):
        actual = find_repeat([1, 2, 5, 5, 5, 5])
        expected = 5
        self.assertEqual(actual, expected)

    def test_long_list(self):
        actual = find_repeat([4, 1, 4, 8, 3, 2, 7, 6, 5])
        expected = 4
        self.assertEqual(actual, expected)


unittest.main(verbosity=2)
