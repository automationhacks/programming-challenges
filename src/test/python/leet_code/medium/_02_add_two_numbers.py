"""
You are given two non-empty linked lists representing two non-negative integers. The digits are
stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and
return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example 1:

Input: l1 = [2,4,3], l2 = [5,6,4] Output: [7,0,8] Explanation: 342 + 465 = 807.

Example 2:

Input: l1 = [0], l2 = [0] Output: [0]

Example 3:

Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9] Output: [8,9,9,9,0,0,0,1]

Constraints:

    The number of nodes in each linked list is in the range [1, 100].
    0 <= Node.val <= 9
    It is guaranteed that the list represents a number that does not have leading zeros.

"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, list1: ListNode, list2: ListNode) -> ListNode:
        # Init result linked list and keep a pointer to the tail
        result = ListNode()
        result_tail = result

        carry = 0
        while list1 or list2 or carry:
            # Assume defaults in case we run over one list (i.e. one list > the other list)
            val1 = list1.val if list1 else 0
            val2 = list2.val if list2 else 0

            total = val1 + val2 + carry
            # Use divmod to get no % 10 and no // 10
            carry, to_add = divmod(total, 10)

            # Add new node to the tail of the linked list
            result_tail.next = ListNode(to_add)
            # Reset the tail
            result_tail = result_tail.next

            # We might have run over and seen one list as None.
            # None.next would be an exception and thus this block
            # guards against that.
            list1 = list1.next if list1 else None
            list2 = list2.next if list2 else None

        return result.next
