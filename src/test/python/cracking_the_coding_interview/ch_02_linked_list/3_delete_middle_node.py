"""
Chapter 2: Linked lists
Problem 2.3

Delete Middle Node: Implement an algorithm to delete a node in the middle
(i.e., any node but the first and last node, not necessarily the exact middle) of a singly linked list,
given only access to that node.

EXAMPLE
Input: the node c from the linked list a - >b- >c - >d - >e- >f
Result: nothing is returned, but the new linked list looks like a - >b- >d - >e- >f
Hints: #72

Picture the list 1 => 5 => 9 =>12. Removing 9 would make it look like 1 => 5 =>12.You only
have access to the 9th node. Can you make it look like the correct answer?
"""

from python.cracking_the_coding_interview.linked_list import LinkedList


def delete_middle_node(node):
    node.value = node.next.value
    node.next = node.next.next


def test_delete_node():
    ll = LinkedList()
    ll.add_multiple([1, 2, 3, 4])
    middle_node = ll.add(5)
    ll.add_multiple([7, 8, 9])

    print(ll)
    delete_middle_node(middle_node)
    print(ll)
