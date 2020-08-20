import unittest

"""
Problem statement

You created a game that is more popular than Angry Birds.

Each round, players receive a score between 0 and 100, which you use to rank them from highest to
lowest. So far you're using an algorithm that sorts in O(nlg⁡n) time, but players are complaining
that their rankings aren't updated fast enough. You need a faster sorting algorithm.

Write a function that takes:

    a list of unsorted_scores
    the highest_possible_score in the game

and returns a sorted list of scores in less than O(nlg⁡n) time.

For example:

unsorted_scores = [37, 89, 41, 65, 91, 53] HIGHEST_POSSIBLE_SCORE = 100

# Returns [91, 89, 65, 53, 41, 37]

sort_scores(unsorted_scores, HIGHEST_POSSIBLE_SCORE)

We’re defining n as the number of unsorted_scores because we’re expecting the number of players to
keep climbing.

And, we'll treat highest_possible_score as a constant instead of factoring it into our big O time
and space costs because the highest possible score isn’t going to change. Even if we do redesign the
game a little, the scores will stay around the same order of magnitude.
"""

"""
Solution

We use counting sort. 
"""


# O(n) space and time
def sort_scores(unsorted_scores, highest_possible_score):
    # Sort the scores in O(n) time
    counts = [0] * (highest_possible_score + 1)

    for score in unsorted_scores:
        counts[score] += 1

    sorted_scores = []

    for idx in range(len(counts) - 1, -1, -1):
        occurences = counts[idx]

        for i in range(occurences):
            sorted_scores.append(idx)

    return sorted_scores


# Tests

class Test(unittest.TestCase):

    def test_no_scores(self):
        actual = sort_scores([], 100)
        expected = []
        self.assertEqual(actual, expected)

    def test_one_score(self):
        actual = sort_scores([55], 100)
        expected = [55]
        self.assertEqual(actual, expected)

    def test_two_scores(self):
        actual = sort_scores([30, 60], 100)
        expected = [60, 30]
        self.assertEqual(actual, expected)

    def test_many_scores(self):
        actual = sort_scores([37, 89, 41, 65, 91, 53], 100)
        expected = [91, 89, 65, 53, 41, 37]
        self.assertEqual(actual, expected)

    def test_repeated_scores(self):
        actual = sort_scores([20, 10, 30, 30, 10, 20], 100)
        expected = [30, 30, 20, 20, 10, 10]
        self.assertEqual(actual, expected)
