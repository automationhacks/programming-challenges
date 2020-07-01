"""
**2.2 Kth to last** Implement an algorithm to find the kth to last element of a singly linked list.

Hints: #8, #25, #47, #67, # 726

- What if you knew the linked list size? What is the difference between finding the Kth-to- last element and finding the Xth element?
- If you don't know the linked list size, can you compute it? How does this impact the runtime?
- Look at this graph. Is there any node you can identify that will definitely be okay to build first?
- You might find it useful to return multiple values. Some languages don't directly support this, but there are workarounds in essentially any language. What are some of those workarounds?
- We're probably going to run this algorithm many times. If we did more preprocessing, is there a way we could optimize this?

[Official solution](https://github.com/careercup/CtCI-6th-Edition-Python/blob/master/Chapter2/2_Return_Kth_To_Last.py)
"""
from python.cracking_the_coding_interview.linked_list import LinkedList


def kth_to_last(ll, k):
    if ll.head is None:
        return

    length = 0
    current = ll.head
    while current:
        length += 1
        current = current.next

    stop = length - k
    index = 0

    current = ll.head
    while current:
        if index == stop:
            return current.value
        else:
            current = current.next
            index += 1

    return None


def kth_to_last_runner(ll, k):
    """
    Runner technique:
    current: points to head
    runner: runs till kth position
    Once reached, both current and runner move till runner reaches the end
    We then can return the data at the current's position
    then runner is increamen
    :param ll:
    :param k:
    :return:
    """
    if ll.head is None:
        return

    runner = current = ll.head
    for i in range(k):
        if runner is None:
            return None
        runner = runner.next

    while runner:
        current = current.next
        runner = runner.next

    return current.value


def test_kth_to_last():
    ll = LinkedList()
    ll.generate(6, 0, 99)
    k = 3
    print()
    print(f'Given LL: {ll} and k: {k}')
    value = kth_to_last(ll, k)
    print(value)
    value = kth_to_last_runner(ll, k)
    print(value)
