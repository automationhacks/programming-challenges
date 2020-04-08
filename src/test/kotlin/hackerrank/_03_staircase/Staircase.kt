package hackerrank._03_staircase

import java.util.*

// Complete the staircase function below.

/*
Logic:

spaces = 5, star = 1
spaces = 4, star = 2
spaces = 3, star = 3
...
*/
fun staircase(totalColumns: Int) {
    for (row in totalColumns downTo 1) {
        val spaces = row - 1
        val star = totalColumns - spaces

        for (temp in 0 until spaces) {
            print(" ")
        }

        for (temp in 0 until star) {
            print("#")
        }

        println()
    }
}

fun main() {
    val scan = Scanner(System.`in`)
    val n = scan.nextLine().trim().toInt()

    staircase(n)
}
