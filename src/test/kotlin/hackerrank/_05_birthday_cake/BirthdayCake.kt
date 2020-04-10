package hackerrank._05_birthday_cake

import java.io.*
import java.math.*
import java.security.*
import java.text.*
import java.util.*
import java.util.concurrent.*
import java.util.function.*
import java.util.regex.*
import java.util.stream.*
import kotlin.collections.*
import kotlin.comparisons.*
import kotlin.io.*
import kotlin.jvm.*
import kotlin.jvm.functions.*
import kotlin.jvm.internal.*
import kotlin.ranges.*
import kotlin.sequences.*
import kotlin.text.*

fun birthdayCakeCandles(ar: Array<Int>): Int? {
    val candleHeightMapping = hashMapOf<Int, Int>()

    for (candleHeight in ar) {
        incrementMapValue(candleHeightMapping, candleHeight)
    }

    val max : Int = candleHeightMapping.keys.max() ?: 0
    return candleHeightMapping[max]
}

fun incrementMapValue(aMap : HashMap<Int, Int>, key : Int) : HashMap<Int, Int> {
    val value = aMap.getOrDefault(key, 0)
    aMap[key] = value + 1
    return aMap
}

fun main() {
    val scan = Scanner(System.`in`)
    val ar = scan.nextLine().split(" ").map{ it.trim().toInt() }.toTypedArray()
    val result = birthdayCakeCandles(ar)

    println(result)
}
