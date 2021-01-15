"""
Source: Leetcode
Difficulty: Medium
Link: https://leetcode.com/problems/max-area-of-island/
Topic: Array, DFS

Given a non-empty 2D array grid of 0's and 1's, an island is a group of 1's (representing land)
connected 4-directionally (horizontal or vertical.) You may assume all four edges of the grid are
surrounded by water.

Find the maximum area of an island in the given 2D array. (If there is no island, the maximum area
is 0.)

Example 1:

```
[[0,0,1,0,0,0,0,1,0,0,0,0,0],
 [0,0,0,0,0,0,0,1,1,1,0,0,0],
 [0,1,1,0,1,0,0,0,0,0,0,0,0],
 [0,1,0,0,1,1,0,0,1,0,1,0,0],
 [0,1,0,0,1,1,0,0,1,1,1,0,0],
 [0,0,0,0,0,0,0,0,0,0,1,0,0],
 [0,0,0,0,0,0,0,1,1,1,0,0,0],
 [0,0,0,0,0,0,0,1,1,0,0,0,0]]
```

Given the above grid, return 6. Note the answer is not 11, because the island must be connected
4-directionally.

Example 2:

[[0,0,0,0,0,0,0,0]]

Given the above grid, return 0.

Note: The length of each dimension in the given grid does not exceed 50.
"""

from typing import List

"""
## Approach

- Scan the islands one cell at a time
- Keep track of cells that are visited in a seen set
- Check if current x, y co-ordinate is within bounds of the island and if not return 0
  - x is not the first, last row, 
  - y is not first and last col
  - x, y is not already seen
  - cell at x, y is land (i.e. > 0)
- Otherwise, count current cell and then recurse in a DFS manner on all the four directions
- Return the max area
  
## Complexity:

- Time: O(R * C), R is no of rows, C is no cols, we visit each square exactly once
- Space: O(R * C), space needed by `seen` to keep track of visited squares and space used by call stack during recursion
"""


class Solution:
    def maxAreaOfIsland(self, island: List[List[int]]) -> int:
        seen = set()

        def dfs(x, y):
            if not (0 <= x < rows and 0 <= y < cols and (x, y) not in seen and island[x][y]):
                return 0
            seen.add((x, y))

            return 1 + dfs(x + 1, y) + dfs(x - 1, y) + dfs(x, y - 1) + dfs(x, y + 1)

        max_area = 0
        rows = len(island)
        cols = len(island[0])
        for row in range(rows):
            for col in range(cols):
                max_area = max(max_area, dfs(row, col))

        return max_area


def test_max_area_of_short_island():
    islands = [[1, 1, 0, 0, 0], [1, 1, 0, 0, 0], [0, 0, 0, 1, 1], [0, 0, 0, 1, 1]]
    assert Solution().maxAreaOfIsland(islands) == 4


def test_max_area_of_island():
    islands = [[0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
               [0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
               [0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0],
               [0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0]]
    assert Solution().maxAreaOfIsland(islands) == 6


def test_one_input():
    island = [[1]]
    assert Solution().maxAreaOfIsland(island) == 1
