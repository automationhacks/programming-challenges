"""
CH2 2.7 Intersection: Given two (singly) linked lists, determine if the two lists intersect. Return the inter- secting
node. Note that the intersection is defined based on reference, not value. That is, if the kth node of the first linked
list is the exact same node (by reference) as the jth node of the second linked list, then they are intersecting.
Hints: #20, #45, #55, #65, #76, #93, #111, #120, #129

a => b => d => c => e | 5
a => b => f => g => h => c => e | 7

You can do this in 0 (A+B) time and 0 (1) additional space. That is, you do not need a hash table
(although you could do it with one).

Examples will help you. Draw a picture of intersecting linked lists and two equivalent
linked lists (by value) that do not intersect

Focus first on just identifying if there's an intersection.

Observe that two intersecting linked lists will always have the same last node. Once they intersect,
all the nodes after that will be equal.

You can determine if two linked lists intersect by traversing to the end of each and comparing their tails.

Now, you need to find where the linked lists intersect. Suppose the linked lists were the
same length. How could you do this?

If the two linked lists were the same length, you could traverse forward in each until you found an element in common.
Now, how do you adjust this for lists of different lengths?

Try using the difference between the lengths of the two linked lists

If you move a pointer in the longer linked list forward by the difference in lengths, you can then apply
a similar approach to the scenario when the linked lists are equal.
"""


def intersection(list1, list2):
    if list1.tail is not list2.tail:
        return False

    list1_len = len(list1)
    list2_len = len(list2)

    shorter = list1 if list1_len < list2_len else list2
    longer = list1 if list1_len > list2_len else list2

    diff = len(longer) - len(shorter)

    shorter_node, longer_node = shorter.head, longer.head

    for i in range(diff):
        longer_node = longer_node.next

    while shorter_node is not longer_node:
        shorter_node = shorter_node.next
        longer_node = longer_node.next

    return longer_node
