"""
Source: Leetcode
Difficulty: Easy
Link: https://leetcode.com/problems/island-perimeter/
Topic: Matrix

You are given row x col grid representing a map where grid[i][j] = 1 represents land and grid[i][j]
= 0 represents water.

Grid cells are connected horizontally/vertically (not diagonally). The grid is completely surrounded
by water, and there is exactly one island (i.e., one or more connected land cells).

The island doesn't have "lakes", meaning the water inside isn't connected to the water around the
island. One cell is a square with side length 1. The grid is rectangular, width and height don't
exceed 100. Determine the perimeter of the island.

```text
Input: grid = [[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]
Output: 16
Explanation: The perimeter is the 16 yellow stripes in the image above.

Example 2:

Input: grid = [[1]]
Output: 4

Example 3:

Input: grid = [[1,0]]
Output: 4
```

Constraints:

- row == grid.length
- col == grid[i].length
- 1 <= row, col <= 100
- grid[i][j] is 0 or 1.
"""

from typing import List


class Solution:
    # Time O(mn), m is no of rows, n is no of cols in the grid
    # Space O(1), since only perimeter variable is updated
    # Approach:
    # Simple counting
    # Iterate in the matrix and if you get a land cell, check its neighbours
    # Every cell can have max perimeter of 4 and we subtract the left, right, up, down cells (which can only have 1)
    # while considering the first row, last row, first col and last col as edges wherein we set left, right, up,
    # down as 0 since there is nothing beyond that on the map
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])

        land = 1
        perimeter = 0

        for row in range(rows):
            for col in range(cols):
                current_cell = grid[row][col]

                if current_cell == land:
                    if row == 0:
                        up = 0
                    else:
                        up = grid[row - 1][col]

                    if col == 0:
                        left = 0
                    else:
                        left = grid[row][col - 1]

                    if row == rows - 1:
                        down = 0
                    else:
                        down = grid[row + 1][col]

                    if col == cols - 1:
                        right = 0
                    else:
                        right = grid[row][col + 1]

                    perimeter += 4 - (up + down + left + right)

        return perimeter


def test_island_perimeter():
    assert Solution().islandPerimeter([[0, 1, 0, 0], [1, 1, 1, 0], [0, 1, 0, 0], [1, 1, 0, 0]]) == 16
