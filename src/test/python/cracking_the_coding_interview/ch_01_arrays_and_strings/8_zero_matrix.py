"""
CTCI 6th edition: Chapter 1: Arrays and Strings, Problem 1.8

Zero Matrix: Write an algorithm such that if an element in an MxN matrix is 0, its entire row and column are set to O.
Hints: # 17, #74, #102

Hints:
- If you just cleared the rows and columns as you found Os, you'd likely wind up clearing the whole matrix.Try finding
the cells with zeros first before making any changes to the matrix.
- Can you use O(N) additional space instead of O(N2)? What information do you really need from the
list of cells that are zero?
- You probably need some data storage to maintain a list of the rows and columns that need to be zeroed. Can you reduce
the additional space usage to a(1) by using the matrix itself for data storage?

Official solution: https://github.com/careercup/CtCI-6th-Edition-Python/blob/master/Chapter1/8_Zero%20Matrix/ZeroMatrix.py

"""


# O(M * N)
def zero_matrix(matrix):
    to_zero_rows = set()
    to_zero_cols = set()

    rows = len(matrix)
    cols = len(matrix[0])

    for x in range(rows):
        for y in range(cols):
            if matrix[x][y] == 0:
                to_zero_rows.add(x)
                to_zero_cols.add(y)

    for row in to_zero_rows:
        for col in range(cols):
            matrix[row][col] = 0

    for col in to_zero_cols:
        for row in range(rows):
            matrix[row][col] = 0

    return matrix


def test_zero_matrix():
    data = [
        ([
             [1, 2, 3, 4, 0],
             [6, 0, 8, 9, 10],
             [11, 12, 13, 14, 15],
             [16, 0, 18, 19, 20],
             [21, 22, 23, 24, 25]
         ], [
             [0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0],
             [11, 0, 13, 14, 0],
             [0, 0, 0, 0, 0],
             [21, 0, 23, 24, 0]
         ])
    ]

    for test_matrix, expected in data:
        assert zero_matrix(test_matrix) == expected
