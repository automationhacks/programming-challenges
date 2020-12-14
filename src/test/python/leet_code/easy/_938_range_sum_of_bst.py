"""
LC Easy 938 Range Sum of BST
https://leetcode.com/problems/range-sum-of-bst/

Given the root node of a binary search tree, return the sum of values of all nodes with a value in
the range [low, high].

Input: root = [10,5,15,3,7,null,18], low = 7, high = 15 Output: 32

Constraints:

- The number of nodes in the tree is in the range [1, 2 * 104].
- 1 <= Node.val <= 105
- 1 <= low <= high <= 105
- All Node.val are unique.
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Approach: Use DFS to walk in the tree and only recurse if the value of node > low and < high
# Making use of BST property where every node to left is less than parent
# And every node on right is greater than the parent

# Time: O(n)
# Space: O(n)

class Solution:
    def rangeSumBST(self, root: TreeNode, low: int, high: int) -> int:
        def get_sum(node):
            if node:
                if low <= node.val <= high:
                    self.total += node.val

                if low < node.val:
                    get_sum(node.left)

                if node.val < high:
                    get_sum(node.right)

        self.total = 0
        get_sum(root)
        return self.total