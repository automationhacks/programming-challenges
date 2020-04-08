package hackerrank._02_plus_minus

import org.testng.annotations.Test
import java.math.RoundingMode
import java.util.*
import kotlin.collections.*

/*
Given an array of integers, calculate the fractions of its elements that are positive, negative, and are zeros. Print the decimal value of each fraction on a new line.

Note: This challenge introduces precision problems. The test cases are scaled to six decimal places, though answers with absolute error of up to  are acceptable.

For example, given the array  there are  elements, two positive, two negative and one zero. Their ratios would be ,  and . It should be printed as

0.400000
0.400000
0.200000
Function Description

Complete the plusMinus function in the editor below. It should print out the ratio of positive, negative and zero items in the array, each on a separate line rounded to six decimals.

plusMinus has the following parameter(s):

arr: an array of integers
Input Format

The first line contains an integer, , denoting the size of the array.
The second line contains  space-separated integers describing an array of numbers .

Constraints



Output Format

You must print the following  lines:

A decimal representing of the fraction of positive numbers in the array compared to its size.
A decimal representing of the fraction of negative numbers in the array compared to its size.
A decimal representing of the fraction of zeros in the array compared to its size.
Sample Input

6
-4 3 -9 0 4 1
Sample Output

0.500000
0.333333
0.166667
Explanation

There are  positive numbers,  negative numbers, and  zero in the array.
The proportions of occurrence are positive: , negative:  and zeros: .
 */




class PlusMinusTests {
    private fun plusMinus(arr: Array<Int>): Unit {
        val noMap: HashMap<String, Int> = hashMapOf("positive" to 0, "negative" to 0, "zero" to 0)
        val totalElements = arr.size

        for (elem in arr) {
            when {
                elem > 0 -> {
                    updateValue(noMap, "positive")
                }
                elem < 0 -> {
                    updateValue(noMap, "negative")
                }
                else -> {
                    updateValue(noMap, "zero")
                }
            }
        }

        roundToPrecision(noMap["positive"]!!, totalElements)
        roundToPrecision(noMap["negative"]!!, totalElements)
        roundToPrecision(noMap["zero"]!!, totalElements)
    }

    private fun updateValue(noMap: HashMap<String, Int>, key: String) {
        val temp = noMap[key] ?: 0
        noMap[key] = temp + 1
    }

    private fun roundToPrecision(no: Int, totalElements: Int, precision: Int = 6) {
        val fraction = no / totalElements.toDouble()
        println(fraction.toBigDecimal().setScale(precision, RoundingMode.UP))
    }

    @Test
    fun testPlusMinus() {
        val input = "-4 3 -9 0 4 1".split(" ").map { it.trim().toInt() }.toTypedArray()
        plusMinus(input)
    }
}