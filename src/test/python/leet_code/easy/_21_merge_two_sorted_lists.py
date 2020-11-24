"""
Leet code - Easy problem # 21
https://leetcode.com/problems/merge-two-sorted-lists/

Merge two sorted linked lists and return it as a new sorted list. The new list should be made by
splicing together the nodes of the first two lists.

Input: l1 = [1,2,4], l2 = [1,3,4] Output: [1,1,2,3,4,4]

Example 2:

Input: l1 = [], l2 = [] Output: []

Example 3:

Input: l1 = [], l2 = [0] Output: [0]

Constraints:

    The number of nodes in both lists is in the range [0, 50].
    -100 <= Node.val <= 100
    Both l1 and l2 are sorted in non-decreasing order.
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        # Keep a pointer to the head
        prehead = ListNode(-1)
        # prev keeps a pointer to the prev element in the merged list
        prev = prehead

        # Notice we go on only if both the lists have elements
        while l1 and l2:
            # On every iteration we check which node has smaller value and then connect it to prev
            # (which is tracking the merged list) and then move the pointer to the next item in the list where
            # the connection was made
            # Also we keep the prev pointer updated by updating it to next
            if l1.val <= l2.val:
                prev.next = l1
                l1 = l1.next
            else:
                prev.next = l2
                l2 = l2.next

            prev = prev.next

        # Finally when one list becomes null we add the last element from the non null list
        prev.next = l1 if l1 is not None else l2

        # We return the next node to avoid returning the prehead with -1 value
        return prehead.next
