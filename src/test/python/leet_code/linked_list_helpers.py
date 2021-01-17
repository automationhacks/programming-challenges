# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def convert_linked_list_to_list(linked_list):
    result = []

    while linked_list is not None:
        result.append(linked_list.val)
        linked_list = linked_list.next

    return result


def convert_list_to_linked_list(numbers):
    head = ListNode()
    curr = head

    for num in numbers:
        print(num)
        node = ListNode(num)
        curr.next = node
        curr = node

    return head.next
