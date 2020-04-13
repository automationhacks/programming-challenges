package hackerrank._07_array_splitting

/**
 * Given an array [3, 10, -5, 6]
 * Find the max no of ways the array can be split such that sum of LHS > RHS
 * Ex: [3, 10, -5, 6]
 * can be split as:
 * [3], [10, -5, 6] 3 < 11
 * [3, 10], [-5, 6] 13 > 1
 * [3, 10, -5], [6] 8 > 6
 *
 * so the no of times LHS > RHS = 2
 */

fun splitIntoTwo(arr: Array<Int>): Int {
    var timesLeftIsGreater = 0


    val totalElements = arr.size

    // Note: Below code passes the functional tests but does not compile in the speed limit.
    for (index in 1 until totalElements) {
        val leftTotal = arr.getTotalForSubArray(0, index)
        val rightTotal = arr.getTotalForSubArray(index, totalElements)

        if (leftTotal > rightTotal) {
            timesLeftIsGreater += 1
        }
    }

    return timesLeftIsGreater
}

fun Array<Int>.getTotalForSubArray(beginRange : Int, endRange : Int): Int {
    val sliced = this.slice(beginRange until endRange)
    return sliced.reduce {sum, element -> sum + element}
}

fun main() {
    val arr = arrayOf(3, 10, -5, 6)
    val result = splitIntoTwo(arr)
    println(result)
}
