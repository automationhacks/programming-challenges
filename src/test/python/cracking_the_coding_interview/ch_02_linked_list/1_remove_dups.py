"""
**2.1 Remove Dups:** Write code to remove duplicates from an unsorted linked list.
FOLLOW UP
How would you solve this problem if a temporary buffer is not allowed? Hints: #9, #40

Hints:

- Have you tried a hash table? You should be able to do this in a single pass of the linked list.
- Without extra space, you'll need a(N^2) time. Try using two pointers, where the second
one searches ahead of the first one.

[Official solution](https://github.com/careercup/CtCI-6th-Edition-Python/blob/master/Chapter2/1_Remove_Dups.py)
"""
from python.cracking_the_coding_interview.linked_list import LinkedList


def remove_dups(ll):
    if ll.head is None:
        return

    current = ll.head
    seen = {current.value}

    while current.next is not None:
        if current.next.value in seen:
            current.next = current.next.next
        else:
            seen.add(current.next.value)
            current = current.next

    return ll


def remove_dups_follow_up(ll):
    if ll.head is None:
        return

    current = ll.head
    while current:
        runner = current
        while runner.next:
            if runner.next.value == current.value:
                runner.next = runner.next.next
            else:
                runner = runner.next
        current = current.next

    return ll


def test_remove_dups():
    ll = LinkedList()
    ll.generate(20, 0, 9)
    print()
    print(f'Before removing dups {ll}')
    remove_dups(ll)
    print(f'After removing dups {ll}')

    ll.generate(20, 0, 9)
    print()
    print(f'Before removing dups {ll}')
    remove_dups_follow_up(ll)
    print(f'After removing dups {ll}')
