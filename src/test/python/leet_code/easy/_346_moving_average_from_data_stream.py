"""
Source: Leetcode
Difficulty: Easy
Link: https://leetcode.com/problems/moving-average-from-data-stream/
Topic: Data structures (Deque, Circular queue)

Given a stream of integers and a window size, calculate the moving average of all integers in the
sliding window.

Example:

```java
MovingAverage m = new MovingAverage(3);
m.next(1) = 1
m.next(10) = (1 + 10) / 2
m.next(3) = (1 + 10 + 3) / 3
m.next(5) = (10 + 3 + 5) / 3
```
"""

from collections import deque


# Approach: Use a deque
# Time: O(1) appends and popleft happen in constant time
# Space: O(n) where n is the size of the moving window
class MovingAverage:
    def __init__(self, size: int):
        self.numbers = deque()
        self.max_window_size = size
        self.window_sum = 0
        # No of items in the deque
        self.count = 0

    def next(self, val: int) -> float:
        self.count += 1
        self.numbers.append(val)

        tail = self.numbers.popleft() if self.is_full() else 0
        self.window_sum = self.window_sum - tail + val

        return self.get_average(val)

    def is_full(self):
        return self.count > self.max_window_size

    def get_average(self, val):
        return self.window_sum / min(self.count, self.max_window_size)


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)

def test_moving_average():
    moving_average = MovingAverage(3)
    assert moving_average.next(1) == 1
    assert moving_average.next(10) == (1 + 10) / 2
    assert moving_average.next(3) == (1 + 10 + 3) / 3
    assert moving_average.next(5) == (10 + 3 + 5) / 3
