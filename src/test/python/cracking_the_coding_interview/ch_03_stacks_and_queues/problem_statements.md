# Chapter 3: Stacks and queues

## Problem 3.1

- Three in One: Describe how you could use a single array to implement three stacks. 

- Hints: #2, #72, #38, #58
- A stack is simply a data structure in which the most recently added elements are removed first. Can you simulate a single stack using an array? Remember that there are many possible solutions, and there are tradeoffs of each.
- Picture the list 1 => 5 => 9 => 12. Removing 9 would make it look like 1 => 5 => 12.You only have access to the 9 node. Can you make it look like the correct answer?
- If you want to allow for flexible divisions, you can shift stacks around. Can you ensure that all available capacity is used?
- Try thinking about the array as circular, such that the end of the array "wraps around" to the start of the array.

## Problem 3.2

- Stack Min: How would you design a stack which, in addition to push and pop, has a function min which returns the minimum element? Push, pop and min should all operate in 0(1) time.

- Hints: #27, #59, #78

- Observe that the minimum element doesn't change very often. It only changes when a smaller element is added, or when the smallest element is popped.
- What if we kept track of extra data at each stack node? What sort of data might make it easier to solve the problem?
- Consider having each node know the minimum of its "substack" (all the elements beneath it, including itself).

## Problem 3.3

- Stack of Plates: Imagine a (literal) stack of plates. If the stack gets too high, it might topple. Therefore, in real life, we would likely start a new stack when the previous stack exceeds some threshold. 

- Implement a data structure SetOfStacks that mimics this. SetOfStacks should be composed of several stacks and should create a new stack once the previous one exceeds capacity. 

- SetOfStacks.push() and SetOfStacks.pop() should behave identically to a single stack (that is, pop() should return the same values as it would if there were just a single stack).

- FOLLOW UP Implement function popAt(int index)which performs a pop operation on a specific sub-stack. 

- Hints: #64, #87

- You will need to keep track of the size of each substack. When one stack is full, you may need to create a new stack.
- What work is duplicated in the current brute-force algorithm?

- [Official solution](https://github.com/careercup/CtCI-6th-Edition-Python/blob/master/Chapter3/33StackOfPlates.py)

## Problem 3.4

Queue via Stacks: Implement a MyQueue class which implements a queue using two stacks.
Hints: #98, #114

Hints:
- The major difference between a queue and a stack is the order of elements. A queue removes the oldest item and a stack removes the newest item. How could you remove the oldest item from a stack if you only had access to the newest item?
- We can remove the oldest item from a stack by repeatedly removing the newest item (inserting those into the temporary stack) until we get down to one element. Then, after we've retrieved the newest item, putting all the elements back. The issue with this is that doing several pops in a row will require 0 (N) work each time. Can we optimize for scenarios where we might do several pops in a row?

## Problem 3.5

Sort Stack: Write a program to sort a stack such that the smallest items are on the top. You can use an additional temporary stack, but you may not copy the elements into any other data structure (such as an array). The stack supports the following operations: push, pop, peek, and isEmpty.
Hints: # 75, #32, #43

- Alternatively, you could pick a random depth to traverse to and then randomly traverse, stopping when you get to that depth. Think this through, though. Does this work?
- Imagine your secondary stack is sorted. Can you insert elements into it in sorted order? You might need some extra storage. What could you use for extra storage?
- Keep the secondary stack in sorted order, with the biggest elements on the top. Use the primary stack for additional storage.
