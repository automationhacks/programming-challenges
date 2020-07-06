# Trees and graphs problem statements

## 4.1 Route Between Nodes

Given a directed graph, design an algorithm to find out whether there is a route between two nodes.

Hints: #127

- Two well-known algorithms can do this. What are the tradeoffs between them?

## 4.2 List of depths

Given a binary tree, design an algorithm which creates a linked list of all the nodes at each depth (e.g. if you have a tree with depth 0, you'll have 0 linked lists).
Hints: #107, #123, #135

- Try modifying a graph search algorithm to track the depth from the root.
- A hash table or array that maps from level number to nodes at that level might also be useful.
- You should be able to come up with an algorithm involving both depth-first search and
breadth-first search.

## 4.3 Check balanced

Check Balanced: Implement a function to check if a binary tree is balanced. For the purposes of this question, a balanced tree is defined to be a tree such that the heights of the two subtrees of any node never differ by more than one.
Hints : #27, #33 , #49 , #105 , #124

## 4.4 Validate BST

Implement a function to check if a binary tree is a binary search tree. 
Hints: #35, #57, #86, # 113, # 128

- If you traversed the tree using an in-order traversal and the elements were truly in the right order, does this indicate that the tree is actually in order? What happens for duplicate elements? If duplicate elements are allowed, they must be on a specific side (usually the left).
- To be a binary search tree, it's not sufficient that the left.value <= current.value < right.value for each node. Every node on the left must be less than the current node, which must be less than all the nodes on the right.
- If every node on the left must be less than or equal to the current node, then this is really the same thing as saying that the biggest node on the left must be less than or equal to the current node.
- Rather than validating the current node's value against leftTree.max and rightTree.min, can we flip around the logic? Validate the left tree's nodes to ensure that they are smaller than current.value
- Think about the checkBST function as a recursive function that ensures each node is within an allowable (min, max) range. At first, this range is infinite. When we traverse to the left, the min is negative infinity and the max is root. Can you implement this recursive function and properly adjust these ranges as you traverse the tree?
