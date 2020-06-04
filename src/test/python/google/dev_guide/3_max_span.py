"""
Source: https://codingbat.com/prob/p189576

Consider the leftmost and right most appearances of some value in an array.
We'll say that the "span" is the number of elements between the two inclusive.
A single value has a span of 1.
Returns the largest span found in the given array. (Efficiency is not a priority.)

maxSpan([1]) -> 1
maxSpan([1, 2, 1]) -> 3
maxSpan([1, 2, 1, 1, 3]) → 4
maxSpan([1, 4, 2, 1, 4, 1, 4]) → 6
maxSpan([1, 4, 2, 1, 4, 4, 4]) → 6

Additional:
Geek for Geeks: https://www.geeksforgeeks.org/maximum-distance-two-occurrences-element-array/
"""


def max_span(arr):
    curr_max = 0

    for i in range(0, len(arr)):
        for j in range(len(arr) - 1, i, -1):
            if arr[i] == arr[j]:
                span = j - i + 1
                if span > curr_max:
                    curr_max = span

    return curr_max


def max_span_optimized(arr):
    # Store if we have seen the no before
    span_map = {}
    curr_max = 0

    for index, num in enumerate(arr):
        if num in span_map:
            # Compute the span between current index and earlier position
            # Add 1 to keep the end inclusive
            span = index - span_map[num] + 1
            curr_max = max(curr_max, span)
        else:
            span_map[num] = index

    return curr_max


def test_max_span():
    assert max_span([]) == 0
    assert max_span([1, 2, 1, 1, 3]) == 4
    assert max_span([1, 4, 2, 1, 4, 1, 4]) == 6
    assert max_span([1, 4, 2, 1, 4, 1, 4]) == 6


def test_max_span_optimized():
    assert max_span_optimized([]) == 0
    assert max_span_optimized([1, 2, 1, 1, 3]) == 4
    assert max_span_optimized([1, 4, 2, 1, 4, 1, 4]) == 6
    assert max_span_optimized([1, 4, 2, 1, 4, 1, 4]) == 6
