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

- Of course, you could convert the linked lists to integers, compute the sum, and then convert it back to a new linked
list. If you did this in an interview, your interviewer would likely accept the answer, and then see if you could do
this without converting it to a number and back.
- Try recursion. Suppose you have two lists, A = 1 - >5 - >9 (representing 951) and B 2- >3- >6- >7 (representing 7632)
, and a function that operates on the remainder of the lists (5 - >9 and 3- >6 - >7). Could you use this to create
the sum method? What is the relationship between sum(1->5->9, 2->3->6->7) and sum(5->9, 3->6->7)?
- Make sure you have considered linked lists that are not the same length.
- Does your algorithm work on linked lists like 9->7->8 and 6->8->5? Double check that.
- For the follow-up question:The issue is that when the linked lists aren't the same length, the head of one linked
list might represent the 1000's place while the other represents the 1D's place. What if you made them the same
length? Is there a way to modify the linked list to do that, without changing the value it represents?
"""
from python.cracking_the_coding_interview.linked_list import LinkedList


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


def sum_list_follow_up(first_ll, second_ll):
    if len(first_ll) < len(second_ll):
        for i in range(len(second_ll) - len(first_ll)):
            first_ll.add_to_beginning(0)
    else:
        for i in range(len(first_ll) - len(second_ll)):
            second_ll.add_to_beginning(0)

    n1, n2 = first_ll.head, second_ll.head
    result = 0
    while n1 or n2:
        result = (result * 10) + n1.value + n2.value
        n1 = n1.next
        n2 = n2.next

    ll = LinkedList()
    ll.add_multiple([int(i) for i in str(result)])
    return ll


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

    print()
    print(sum_list(first, second))
    print(sum_list_follow_up(first, second))
