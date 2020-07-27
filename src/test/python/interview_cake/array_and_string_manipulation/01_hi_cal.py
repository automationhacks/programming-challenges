"""
Problem source: Interview cake
URL: https://www.interviewcake.com/question/python3/merging-ranges?course=fc1&section=array-and-string-manipulation

Your company built an in-house calendar tool called HiCal.
You want to add a feature to see the times in a day when everyone is available.

To do this, you’ll need to know when any team is having a meeting.
In HiCal, a meeting is stored as a tuple of integers (start_time, end_time).
These integers represent the number of 30-minute blocks past 9:00am.

For example:

(2, 3)  # Meeting from 10:00 – 10:30 am
(6, 9)  # Meeting from 12:00 – 1:30 pm

Write a function merge_ranges() that takes a list of multiple meeting time ranges and returns a list of condensed ranges

For example, given:

  [(0, 1), (3, 5), (4, 8), (10, 12), (9, 10)]

your function would return:

  [(0, 1), (3, 8), (9, 12)]

Do not assume the meetings are in order. The meeting times are coming from multiple teams.

Write a solution that's efficient even when we can't put a nice upper bound on the numbers representing our time ranges.
 Here we've simplified our times down to the number of 30-minute slots past 9:00 am. But we want the function to work
 even for very large numbers, like Unix timestamps.

In any case, the spirit of the challenge is to merge meetings where start_time and end_time don't have an upper bound.
"""

import unittest


def merge_ranges(meetings):
    # Sort by start time
    sorted_meetings = sorted(meetings)

    # Init merged meetings with the earliest meeting
    merged_meetings = [sorted_meetings[0]]

    for current_meeting_start, current_meeting_end in sorted_meetings[1:]:
        last_merged_meeting_start, last_merged_meeting_end = merged_meetings[-1]

        # If the current meeting overlaps with the last merged meeting,
        # use the later end time of the two
        if current_meeting_start <= last_merged_meeting_end:
            merged_meetings[-1] = (last_merged_meeting_start, max(last_merged_meeting_end, current_meeting_end))
        else:
            # Add the current meeting since it does not overlap
            merged_meetings.append((current_meeting_start, current_meeting_end))
    return merged_meetings


# Tests
class Test(unittest.TestCase):

    def test_meetings_overlap(self):
        actual = merge_ranges([(1, 3), (2, 4)])
        expected = [(1, 4)]
        self.assertEqual(actual, expected)

    def test_meetings_touch(self):
        actual = merge_ranges([(5, 6), (6, 8)])
        expected = [(5, 8)]
        self.assertEqual(actual, expected)

    def test_meeting_contains_other_meeting(self):
        actual = merge_ranges([(1, 8), (2, 5)])
        expected = [(1, 8)]
        self.assertEqual(actual, expected)

    def test_meetings_stay_separate(self):
        actual = merge_ranges([(1, 3), (4, 8)])
        expected = [(1, 3), (4, 8)]
        self.assertEqual(actual, expected)

    def test_multiple_merged_meetings(self):
        actual = merge_ranges([(1, 4), (2, 5), (5, 8)])
        expected = [(1, 8)]
        self.assertEqual(actual, expected)

    def test_meetings_not_sorted(self):
        actual = merge_ranges([(5, 8), (1, 4), (6, 8)])
        expected = [(1, 4), (5, 8)]
        self.assertEqual(actual, expected)

    def test_one_long_meeting_contains_smaller_meetings(self):
        actual = merge_ranges([(1, 10), (2, 5), (6, 8), (9, 10), (10, 12)])
        expected = [(1, 12)]
        self.assertEqual(actual, expected)

    def test_sample_input(self):
        actual = merge_ranges([(0, 1), (3, 5), (4, 8), (10, 12), (9, 10)])
        expected = [(0, 1), (3, 8), (9, 12)]
        self.assertEqual(actual, expected)


"""
Solution:

First, we sort our input list of meetings by start time so any meetings that might need to be merged are now next to 
each other.

Then we walk through our sorted meetings from left to right. At each step, either:

- We can merge the current meeting with the previous one, so we do.
- We can't merge the current meeting with the previous one, so we know the previous meeting can't be merged with any 
future meetings and we throw the current meeting into merged_meetings.

Complexity analysis:

O(n log(n)) time and O(n)) space.

Even though we only walk through our list of meetings once to merge them, we sort all the meetings first, 
giving us a runtime of O(n log(n)). It's worth noting that if our input were sorted, we could skip the sort and do 
this in O(n) time!

We create a new list of merged meeting times. In the worst case, none of the meetings overlap, giving us a list 
identical to the input list. Thus we have a worst-case space cost of O(n). 


This one arguably uses a greedy approach as well, except this time we had to sort the list first.

How did we figure that out?

We started off trying to solve the problem in one pass, and we noticed that it wouldn't work. 
We then noticed the reason it wouldn't work: to see if a given meeting can be merged, we have to look at all the 
other meetings! That's because the order of the meetings is random.

That's what got us thinking: what if the list were sorted? We saw that then a greedy approach would work. 
We had to spend O(n log(n)) time on sorting the list, but it was better than our initial brute force approach, 
which cost us O(n^2) time!
"""
