"""
Write a function to check that a binary tree is a valid binary search tree.
"""

import unittest

import sys

"""
Approach:

A binary tree is a BST 

- if node on left is lesser than ancestor
- if node on right is greater than ancestor

We do a DFS walk by using a stack and check if the node falls within desired bounds

Complexity:

- Time: O(n), since in worst case we would visit each node
- Space: O(n), since we need to hold at most d nodes (d is the depth of the tree), in worst case it could be a 
  straight line on the right nodes with one left node, thus on the rightmost node the space would be O(d) which 
  is ~ close to O(n)
"""


def is_binary_search_tree(root):
    # Start with root having an arbitrarily low and high bounds
    node_and_bounds_stack = [(root, -sys.maxsize, sys.maxsize)]

    while len(node_and_bounds_stack):
        node, lower_bound, upper_bound = node_and_bounds_stack.pop()

        # Check if node value is not within bounds
        if node.value <= lower_bound or node.value >= upper_bound:
            return False

        if node.left:
            # left node must be lesser than parent, thus parent becomes upper bound
            node_and_bounds_stack.append((node.left, lower_bound, node.value))

        if node.right:
            # right node must be greater than parent, thus parent becomes lower bound
            node_and_bounds_stack.append((node.right, node.value, upper_bound))

    return True


# recursive impl (prone to stack overflow)
def is_binary_search_tree(root, lower_bound=-sys.maxsize, upper_bound=sys.maxsize):
    if not root:
        return True

    if root.value <= lower_bound or root.value >= upper_bound:
        return False

    return is_binary_search_tree(root.left, lower_bound, root.value) and is_binary_search_tree(root.right, root.value,
                                                                                               upper_bound)


# Tests
class Test(unittest.TestCase):
    class BinaryTreeNode(object):

        def __init__(self, value):
            self.value = value
            self.left = None
            self.right = None

        def insert_left(self, value):
            self.left = Test.BinaryTreeNode(value)
            return self.left

        def insert_right(self, value):
            self.right = Test.BinaryTreeNode(value)
            return self.right

    def test_valid_full_tree(self):
        tree = Test.BinaryTreeNode(50)
        left = tree.insert_left(30)
        right = tree.insert_right(70)
        left.insert_left(10)
        left.insert_right(40)
        right.insert_left(60)
        right.insert_right(80)
        result = is_binary_search_tree(tree)
        self.assertTrue(result)

    def test_both_subtrees_valid(self):
        tree = Test.BinaryTreeNode(50)
        left = tree.insert_left(30)
        right = tree.insert_right(80)
        left.insert_left(20)
        left.insert_right(60)
        right.insert_left(70)
        right.insert_right(90)
        result = is_binary_search_tree(tree)
        self.assertFalse(result)

    def test_descending_linked_list(self):
        tree = Test.BinaryTreeNode(50)
        left = tree.insert_left(40)
        left_left = left.insert_left(30)
        left_left_left = left_left.insert_left(20)
        left_left_left.insert_left(10)
        result = is_binary_search_tree(tree)
        self.assertTrue(result)

    def test_out_of_order_linked_list(self):
        tree = Test.BinaryTreeNode(50)
        right = tree.insert_right(70)
        right_right = right.insert_right(60)
        right_right.insert_right(80)
        result = is_binary_search_tree(tree)
        self.assertFalse(result)

    def test_one_node_tree(self):
        tree = Test.BinaryTreeNode(50)
        result = is_binary_search_tree(tree)
        self.assertTrue(result)

# unittest.main(verbosity=2)
