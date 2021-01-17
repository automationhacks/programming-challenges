"""
Source: Leetcode
Difficulty: Easy
Link: https://leetcode.com/problems/toeplitz-matrix/
Topic: Matrix

Given an m x n matrix, return true if the matrix is Toeplitz. Otherwise, return false.

A matrix is Toeplitz if every diagonal from top-left to bottom-right has the same elements.

Example 1:

Input: matrix =
[[1, 2, 3, 4],
 [5, 1, 2, 3],
 [9, 5, 1, 2]]

Output: true Explanation: In the above grid, the
diagonals are: "[9]", "[5, 5]", "[1, 1, 1]", "[2, 2, 2]", "[3, 3]", "[4]". In each diagonal all
elements are the same, so the answer is True.

Example 2:

Input: matrix =
[[1,2],
 [2,2]]

Output: false Explanation: The diagonal "[1, 2]" has different elements.

Constraints:

- m == matrix.length
- n == matrix[i].length
- 1 <= m, n <= 20
- 0 <= matrix[i][j] <= 99

Follow up:

- What if the matrix is stored on disk, and the memory is limited such that you can only load at
  most one row of the matrix into the memory at once?
- What if the matrix is so large that you can only load up a partial row into the memory at once?

"""
from typing import List

"""
Approach

Iterate in the matrix, row by row
Check if the top left cell is equal to current cell
Take care of boundary conditions

Complexity
O(m * n), m => no of rows, n => no of cols
O(1), since we are not storing anything additional

- What if the matrix is stored on disk, and the memory is limited such that you can only load at
  most one row of the matrix into the memory at once?
- What if the matrix is so large that you can only load up a partial row into the memory at once?

Ans: 

- Load only two rows in mem
- This could be an approach for 2nd part https://en.wikipedia.org/wiki/Loop_nest_optimization
"""


class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        row_len = len(matrix)
        for row in range(row_len):
            col_len = len(matrix[0])

            for col in range(col_len):
                if row > 0 and col > 0:
                    current_cell = matrix[row][col]
                    top_left = matrix[row - 1][col - 1]
                    if current_cell != top_left:
                        return False

        return True


def test_matrix_is_toeplitz():
    input = [[1, 2, 3, 4], [5, 1, 2, 3], [9, 5, 1, 2]]
    output = True
    assert Solution().isToeplitzMatrix(input) == output


def test_matrix_is_not_toeplitz():
    input = [[1, 2], [2, 2]]
    output = False
    assert Solution().isToeplitzMatrix(input) == output
