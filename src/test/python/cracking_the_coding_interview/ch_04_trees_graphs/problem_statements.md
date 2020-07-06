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


