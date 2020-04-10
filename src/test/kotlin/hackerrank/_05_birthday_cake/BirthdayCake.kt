package hackerrank._05_birthday_cake

import java.util.*
import kotlin.collections.*

fun birthdayCakeCandles(ar: Array<Int>): Int? {
    val candleHeightMapping = hashMapOf<Int, Int>()

    for (candleHeight in ar) {
        incrementMapValue(candleHeightMapping, candleHeight)
    }

    val max: Int = candleHeightMapping.keys.max() ?: 0
    return candleHeightMapping[max]
}

fun incrementMapValue(aMap: HashMap<Int, Int>, key: Int): HashMap<Int, Int> {
    val value = aMap.getOrDefault(key, 0)
    aMap[key] = value + 1
    return aMap
}

fun main() {
    val scan = Scanner(System.`in`)
    val ar = scan.nextLine().split(" ").map { it.trim().toInt() }.toTypedArray()
    val result = birthdayCakeCandles(ar)

    println(result)
}
