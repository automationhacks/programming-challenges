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
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        l1_copy = l1
        l2_copy = l2

        l1_length = 0
        while l1.next:
            l1_length += 1
            l1 = l1.next

        l2_length = 0
        while l2.next:
            l2_length += 1
            l2 = l2.next

        result = ListNode()

        # If both the nos are of equal length
        if l1_length == l2_length:
            previous_carry = 0
            while l1.next and l2.next:
                total = l1.val + l2.val + previous_carry

                if total > 9:
                    carry = total // 10
                    remainder = total % 10
                    result.val = remainder
                    previous_carry = carry
                else:
                    result.val = total

                l1 = l1.next
                l2 = l2.next
        else:
            if l1_length > l2_length:
                bigger = l1
                smaller = l2
            else:
                bigger = l2
                smaller = l1

            while bigger.next:
                previous_carry = 0

                if smaller.next:
                    total = bigger.val + smaller.val + previous_carry
                else:
                    total = bigger.val + previous_carry

                if total > 9:
                    carry = total // 10
                    remainder = total % 10
                    result.val = remainder
                    previous_carry = carry
                else:
                    result.val = total

                bigger = bigger.next
                smaller = smaller.next

        while result.next:
            print(result.val)

        return result






