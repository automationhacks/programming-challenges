"""
Chapter 2 Linked lists

2.5 Sum Lists: You have two numbers represented by a linked list, where each node contains a single digit.
The digits are stored in reverse order, such that the 1st digit is at the head of the list.

Write a function that adds the two numbers and returns the sum as a linked list.

EXAMPLE
Input: (7 => 1 => 6) + (5 => 9 => 2).That is, 617 + 295.
Output: 2 => 1 => 9.That is, 912.

FOLLOW UP
Suppose the digits are stored in forward order. Repeat the above problem.

EXAMPLE
Input: (6 => 1 => 7) + (2 => 9 => 5).
That is, 617 + 295.
Output: 9 => 1 => 2.
That is, 912.

Hints: #7, #30, #71, #95, #109
"""
from python.cracking_the_coding_interview.ch_02_linked_list.linked_list import LinkedList


def sum_list(first_ll, second_ll):
    carry = 0
    sum_ll = LinkedList()

    first = first_ll.head
    second = second_ll.head

    while first or second:
        to_add, carry = add_nos_with_carry(carry, first, second)

        sum_ll.add(to_add)

        first = first.next
        second = second.next

    return sum_ll


def add_nos_with_carry(carry, first, second):
    first_no = first.value
    second_no = second.value
    total = first_no + second_no + carry
    to_add = total % 10
    carry = total // 10
    return to_add, carry


def test_sum_list():
    first = LinkedList()
    first.add_multiple([7, 1, 6])

    second = LinkedList()
    second.add_multiple([5, 9, 2])

    total = sum_list(first, second)
    print(total)
