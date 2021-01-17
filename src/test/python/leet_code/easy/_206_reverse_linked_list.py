"""
Source: Leetcode
Difficulty: Easy
Link: https://leetcode.com/problems/reverse-linked-list/
Topic: Linked list

Reverse a singly linked list.

Example:

Input: 1->2->3->4->5->NULL
Output: 5->4->3->2->1->NULL

Follow up:

A linked list can be reversed either iteratively or recursively. Could you implement both?
"""
from python.leet_code.linked_list_helpers import *


class Solution:
    """
    Approach: Iterative solution

    Keep track of a previous node (initialized to null in the beginning)
    Keep track of the next node
    Till the head is not pointing to null

    On every iteration
      Set head's next to the previous node
      Set the prev node to head
      And then set head as the next node to continue

    Complexity:
    Time: O(n), since we have to iterate once in the linked list
    Space: O(1), since we only store one extra node
    """
    def reverseList(self, head: ListNode) -> ListNode:
        prev_node = None
        while head is not None:
            next_node = head.next

            head.next = prev_node
            prev_node = head
            head = next_node

        return prev_node


def test_linked_list_reverse():
    numbers = list(range(5))
    expected = numbers[-1::-1]

    input_ll = convert_list_to_linked_list(numbers)
    print(input_ll.val)
    reverse_ll = Solution().reverseList(input_ll)

    result_list = convert_linked_list_to_list(reverse_ll)
    assert result_list == expected
