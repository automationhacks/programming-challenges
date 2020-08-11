import unittest

"""
Problem statement

You've built an inflight entertainment system with on-demand movie streaming.

Users on longer flights like to start a second movie right when their first one ends, 
but they complain that the plane usually lands before they can see the ending. So 
you're building a feature for choosing two movies whose total runtimes will equal the exact flight length.

Write a function that takes an integer flight_length (in minutes) and a list of integers movie_lengths 
(in minutes) and returns a boolean indicating whether there are two numbers in movie_lengths whose sum equals 
flight_length.

When building your function:

    Assume your users will watch exactly two movies
    Don't make your users watch the same movie twice
    Optimize for runtime over memory
"""

"""
Solution:

We make one pass through movie_lengths, treating each item as the first_movie_length. At each iteration, we:

- See if there's a matching_second_movie_length we've seen already (stored in our movie_lengths_seen set) 
that is equal to flight_length - first_movie_length. If there is, we short-circuit and return True.
- Keep our movie_lengths_seen set up to date by throwing in the current first_movie_length.
"""


def can_two_movies_fill_flight(movie_lengths, flight_length):
    # O(n) time and space
    movie_lengths_seen = set()

    for first_movie_length in movie_lengths:
        second_movie_length = flight_length - first_movie_length
        if second_movie_length in movie_lengths_seen:
            return True
        movie_lengths_seen.add(first_movie_length)

    return False


# Tests

class Test(unittest.TestCase):

    def test_short_flight(self):
        result = can_two_movies_fill_flight([2, 4], 1)
        self.assertFalse(result)

    def test_long_flight(self):
        result = can_two_movies_fill_flight([2, 4], 6)
        self.assertTrue(result)

    def test_one_movie_half_flight_length(self):
        result = can_two_movies_fill_flight([3, 8], 6)
        self.assertFalse(result)

    def test_two_movies_half_flight_length(self):
        result = can_two_movies_fill_flight([3, 8, 3], 6)
        self.assertTrue(result)

    def test_lots_of_possible_pairs(self):
        result = can_two_movies_fill_flight([1, 2, 3, 4, 5, 6], 7)
        self.assertTrue(result)

    def test_not_using_first_movie(self):
        result = can_two_movies_fill_flight([4, 3, 2], 5)
        self.assertTrue(result)

    def test_only_one_movie(self):
        result = can_two_movies_fill_flight([6], 6)
        self.assertFalse(result)

    def test_no_movies(self):
        result = can_two_movies_fill_flight([], 2)
        self.assertFalse(result)
