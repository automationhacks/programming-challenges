# Chapter 8: Recursion and Dynamic programming

## Problem 8.1 Triple Step

Triple Step: A child is running up a staircase with n steps and can hop either 1 step, 2 steps, or 3 steps at a time. Implement a method to count how many possible ways the child can run up the stairs.

Hints: # 152, # 178, #217, #237, #262, #359

- Approach this from the top down. What is the very last hop the child made?
- If we knew the number of paths to each of the steps before step 100, could we compute the number of steps to 1OO?
- We can compute the number of steps to 100 by the number of steps to 99, 98, and 97. This corresponds to the child hopping 1, 2, or 3 steps at the end. Do we add those or multiply them? That is: Is it f(l00) = f(99) + f(98) + f(97) or f(100) = f(99) * f(98) * f(97)?
- We multiply the values when it's "we do this then this:' We add them when it's "we do this or this:'
- What is the runtime of this method? Think carefully. Can you optimize it?
- Try memoization as a way to optimize an inefficient recursive program.

## Robot in a grid 

Imagine a robot sitting on the upper left corner of a grid with r rows and c columns. The robot can only move in two directions, right and down, but certain cells are "off limits" such that the robot cannot step on them. Design an algorithm to find a path for the robot from the top left to the bottom right.

Hints: #331, #360, #388

- For the robot to reach the last cell, it must find a path to the second-to-Last cells. For it to find a path to the second-to-Last cells, it must find a path to the third-to-Last cells.
- Simplify this problem a bit by first figuring out if there's a path. Then, modify your algorithm to track the path.
- Think again about the efficiency of your algorithm. Can you optimize it?

