"""
Source: Leetcode
Difficulty: Easy
Link: https://leetcode.com/problems/fibonacci-number/
Topic: Array

The Fibonacci numbers, commonly denoted F(n) form a sequence, called the Fibonacci sequence, such
that each number is the sum of the two preceding ones, starting from 0 and 1. That is,

```
F(0) = 0
F(1) = 1
F(2) = 1
F(n) = F(n - 1) + F(n - 2), for n > 1.
```

Given n, calculate F(n).

```
Example 1:

Input: n = 2
Output: 1
Explanation: F(2) = F(1) + F(0) = 1 + 0 = 1.

Example 2:

Input: n = 3
Output: 2
Explanation: F(3) = F(2) + F(1) = 1 + 1 = 2.

Example 3:

Input: n = 4
Output: 3
Explanation: F(4) = F(3) + F(2) = 2 + 1 = 3.
```

Constraints:

- 0 <= n <= 30
"""
import timeit

from memory_profiler import profile


class Solution:
    # Approach: Recursive
    # Time: O(n)
    # Space: O(n)
    @profile
    def fib_recurse(self, n):
        if n <= 1:
            return n

        return self.fib_recurse(n - 1) + self.fib_recurse(n - 2)

    # Recursive with memoization
    # Time O(n)
    # Space O(n)≠
    def fib_recurse_memo(self, n):
        memo = {0: 0, 1: 1, 2: 1}

        def recurse_with_memo(n):
            if n <= 1:
                return n

            if n in memo:
                return memo[n]
            else:
                result = recurse_with_memo(n - 1) + recurse_with_memo(n - 2)
                memo[n] = result
                return result

        return recurse_with_memo(n)

    # Approach: Iterative top down approach
    # Time: O(n)
    # Space: O(1)
    @profile
    def fib(self, n: int) -> int:
        if n <= 1:
            return n
        if n == 2:
            return 1

        # current = fib(n), prev1 = fib(n-1), prev2 = fib(n-2)
        current = 0
        prev1 = 1
        prev2 = 1

        # Since range is exclusive, to include n, we need to put n + 1
        for i in range(3, n + 1):
            current = prev1 + prev2
            prev1, prev2 = current, prev1

        return current


def test_fibonacci_no():
    fib = Solution().fib_recurse_memo

    assert fib(0) == 0
    assert fib(1) == 1
    assert fib(2) == 1
    assert fib(10) == 55


def test_fibonacci_no_performance():
    fib = Solution().fib_recurse_memo
    start = timeit.default_timer()
    assert fib(10) == 55
    end = timeit.default_timer()
    print(end - start)
