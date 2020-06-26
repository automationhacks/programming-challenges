"""
Chapter 2 Linked lists

2.6 Palindrome: Implement a function to check if a linked list is a palindrome.
Hints: #5, #13, #29, #61, #101

A palindrome is something which is the same when written forwards and backwards. What if you reversed the linked list?

Try using a stack.

Assume you have the length of the linked list. Can you implement this recursively?

In the recursive approach (we have the length of the list), the middle is the base case: isPermutation(middle) is true.The node x to the immediate left of the middle: What can that node do to check if x- >middle- >y forms a palindrome? Now suppose that checks out. What about the previous node a? If x- >middle- >y is a palindrome, how can it check that a - >x - >middle - >y- >b is a palindrome?

Go back to the previous hint. Remember:There are ways to return multiple values. You can do this with a new class.

2 => 3 => 5 => 6 => 5 => 3 => 2
"""
from python.cracking_the_coding_interview.ch_02_linked_list.linked_list import LinkedList


def is_palindrome(ll):
    current = ll.head
    stack = []

    while current:
        stack.append(current.value)
        current = current.next

    current = ll.head

    for i in range(len(ll) // 2):
        if current.value != stack.pop():
            return False
        else:
            current = current.next

    return True


# This is an optimization and O(n) since we only iterate in the
# Linked list only once
def is_palindrome_runner(ll):
    fast = slow = ll.head
    stack = []

    # We store the items till mid point in the stack
    # by making use of a fast runner which reaches the end of the linked list
    # by jumping 2 nodes at a time till we reach the end
    while fast and fast.next:
        stack.append(slow.value)
        slow = slow.next
        fast = fast.next.next

    if fast:
        slow = slow.next

    # Next we iterate in 2nd half of the linked list and compare it with
    # the values already stored in the stack
    while slow:
        top = stack.pop()

        if top != slow.value:
            return False

        slow = slow.next

    return True


def test_is_palidrome():
    data = [
        (LinkedList([2, 3, 5, 6, 5, 3, 2]), True),
        (LinkedList([2, 3, 5, 6, 7, 3, 2]), False),
    ]

    for ll, expected in data:
        assert is_palindrome(ll) is expected
        assert is_palindrome_runner(ll) is expected

