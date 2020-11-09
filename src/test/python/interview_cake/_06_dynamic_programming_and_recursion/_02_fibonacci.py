"""
 Write a function fib() that takes an integer nnn and returns the nnnth Fibonacci ↴ number.

Let's say our Fibonacci series is 0-indexed and starts with 0. So:

  fib(0)  # => 0
fib(1)  # => 1
fib(2)  # => 1
fib(3)  # => 2
fib(4)  # => 3
"""

import unittest


# Top down approach
# O(2^n) time and O(n) space
def fib(n):
    # Compute the nth Fibonacci number
    # 0, 1, 1, 2, 3, 5, 8 ...
    memo = {}
    return fib_rec(n, memo)


def fib_rec(n, memo):
    if n < 0:
        raise Exception('No cannot be negative')

    if n in [0, 1]:
        return n

    if n in memo:
        return memo[n]

    result = fib(n - 1) + fib(n - 2)
    memo[n] = result

    return result


# Tests

class Test(unittest.TestCase):

    def test_zeroth_fibonacci(self):
        actual = fib(0)
        expected = 0
        self.assertEqual(actual, expected)

    def test_first_fibonacci(self):
        actual = fib(1)
        expected = 1
        self.assertEqual(actual, expected)

    def test_second_fibonacci(self):
        actual = fib(2)
        expected = 1
        self.assertEqual(actual, expected)

    def test_third_fibonacci(self):
        actual = fib(3)
        expected = 2
        self.assertEqual(actual, expected)

    def test_fifth_fibonacci(self):
        actual = fib(5)
        expected = 5
        self.assertEqual(actual, expected)

    def test_tenth_fibonacci(self):
        actual = fib(10)
        expected = 55
        self.assertEqual(actual, expected)

    def test_negative_fibonacci(self):
        with self.assertRaises(Exception):
            fib(-1)


unittest.main(verbosity=2)
