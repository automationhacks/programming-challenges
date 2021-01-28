"""
Source: Leetcode
Difficulty: Easy
Link: https://leetcode.com/problems/subtree-of-another-tree/
Topic: Tree

Given two non-empty binary trees s and t, check whether tree t has exactly the same structure and
node values with a subtree of s. A subtree of s is a tree consists of a node in s and all of this
node's descendants. The tree s could also be considered as a subtree of itself.

Example 1:
Given tree s:

     3
    / \
   4   5
  / \
 1   2

Given tree t:

   4
  / \
 1   2

Return true, because t has the same structure and node values with a subtree of s.



Example 2:
Given tree s:

     3
    / \
   4   5
  / \
 1   2
    /
   0

Given tree t:

   4
  / \
 1   2

Return false.
"""

"""
Traverse the tree treating each node as the root and once a matching node is found,
then recurse to compare these subtrees

- Time complexity : O(m*n). In worst case(skewed tree) compare_nodes function takes O(m*n) time.
- Space complexity : O(n). The depth of the recursion tree can go upto n. n refers to the number of nodes in sss.
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSubtree(self, base: TreeNode, to_search: TreeNode) -> bool:
        def compare_nodes(source, target):
            if source is None and target is None:
                return True
            if source is None or target is None:
                return False
            return source.val == target.val and compare_nodes(source.left, target.left) and compare_nodes(source.right,
                                                                                                          target.right)

        stack = [base]

        while len(stack):
            node = stack.pop()

            if node.val == to_search.val:
                found = compare_nodes(node, to_search)
                if found:
                    return True

            if node.left:
                stack.append(node.left)

            if node.right:
                stack.append(node.right)

        return False
