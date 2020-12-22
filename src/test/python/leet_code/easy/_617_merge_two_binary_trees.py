"""
Source: Leetcode
Difficulty: Easy
Link: https://leetcode.com/problems/merge-two-binary-trees/
Topic: Binary tree, DFS/BFS

Given two binary trees and imagine that when you put one of them to cover the other, some nodes of
the two trees are overlapped while the others are not.

You need to merge them into a new binary tree. The merge rule is that if two nodes overlap, then sum
node values up as the new value of the merged node. Otherwise, the NOT null node will be used as the
node of new tree.

Example 1:

```
Input:
	Tree 1                     Tree 2
          1                         2
         / \                       / \
        3   2                     1   3
       /                           \   \
      5                             4   7
Output:
Merged tree:
	     3
	    / \
	   4   5
	  / \   \
	 5   4   7
```

Note: The merging process must start from the root nodes of both trees.
"""


#  Time complexity : O(m). A total of m nodes need to be traversed.
#  Here, m represents the minimum number of nodes from the two given trees.
#  Space complexity : O(m). The depth of the recursion tree can go upto m in the case of a skewed tree.
#  In average case, depth will be O(log m).

# Definition for a binary tree node.

# What did i learn from this:
# In the recursive solution, its better to recurse down the tree and check at the current node level
# instead of doing checks upfront which leads to unnecessary code

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def mergeTrees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
        if t1 is None:
            return t2
        if t2 is None:
            return t1

        t1.val += t2.val
        t1.left = self.mergeTrees(t1.left, t2.left)
        t1.right = self.mergeTrees(t1.right, t2.right)

        return t1
