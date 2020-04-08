package hackerrank._01_diagonal_difference

import org.testng.Assert
import org.testng.annotations.Test
import kotlin.math.abs

/*
Given a square matrix, calculate the absolute difference between the sums of its diagonals.

For example, the square matrix  is shown below:

1 2 3
4 5 6
9 8 9
The left-to-right diagonal = . The right to left diagonal = . Their absolute difference is .

Function description

Complete the  function in the editor below. It must return an integer representing the absolute diagonal difference.

diagonalDifference takes the following parameter:

arr: an array of integers .
Input Format

The first line contains a single integer, , the number of rows and columns in the matrix .
Each of the next  lines describes a row, , and consists of  space-separated integers .

Constraints

Output Format

Print the absolute difference between the sums of the matrix's two diagonals as a single integer.

Sample Input

3
11 2 4
4 5 6
10 8 -12
Sample Output

15
Explanation

The primary diagonal is:

11
   5
     -12
Sum across the primary diagonal: 11 + 5 - 12 = 4

The secondary diagonal is:

     4
   5
10
Sum across the secondary diagonal: 4 + 5 + 10 = 19
Difference: |4 - 19| = 15

Note: |x| is the absolute value of x
 */

/*
 * Complete the 'diagonalDifference' function below.
 *
 * The function is expected to return an INTEGER.
 * The function accepts 2D_INTEGER_ARRAY arr as parameter.
 */



class DiagonalDifferenceTests {
    fun diagonalDifference(arr: Array<Array<Int>>): Int {
        /** Figuring out the logic
        0 1 2
        1 1 2
        2 1 2

        principal diagonal (0, 0), (1, 1), (2, 2)
        secondary diagonal (0, 2), (1, 1), (2, 0)

        row == column -> principal diagonal
        row + column == no of rows - 1 -> secondary diagonal
         */

        var first = 0
        var second = 0

        val noOfRows = arr.size

        for (row in 0 until noOfRows) {
            val elem = arr[row]

            for (column in 0 until elem.size) {
                if (row == column) {
                    first += elem[column]
                }

                if (
                    (row + column) == (noOfRows - 1)) {
                    second += elem[column]
                }
            }
        }
        return abs(first - second)
    }

    @Test
    fun testDiagonalDifference() {
        val inputArr = arrayOf(
            arrayOf(11, 2, 4),
            arrayOf(4, 5, 6),
            arrayOf(10, 8, -12)
        )
        val result = diagonalDifference(inputArr)
        Assert.assertEquals(result, 15)
    }
}

