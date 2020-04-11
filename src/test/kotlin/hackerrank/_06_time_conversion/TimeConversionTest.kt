package hackerrank._06_time_conversion

import org.testng.Assert
import org.testng.annotations.Test

/*
 * Logic
 07:05:45PM
 19:05:45
 *
 * 12 AM - 12 PM
 * 12
 * 01:
 *
 * 11:59:59
 * 12:00:00PM
 *
 * 12 PM - 11:59:59 PM -
 * 1 PM - 13 (1 + 12)
 */
fun timeConversion(s: String): String {
    val timeArray = s.split(":")
    val isBeforeOrAfterNoon = timeArray.last().substring(2)

    val convertedTime = arrayListOf<String>()

    for (idx in 0 until timeArray.size) {
        if (idx == 0) {
            if (isBeforeOrAfterNoon == "PM") {

                if (timeArray[idx] == "12") {
                   convertedTime.add(timeArray[idx])
                }
                else {

                convertedTime.add((timeArray[idx].toInt() + 12).toString())
                }
            } else {
                if (timeArray[idx] == "12") {
                    convertedTime.add("00")
                } else {

                    convertedTime.add(timeArray[idx])
                }
            }
            continue
        }

        if (idx == timeArray.size - 1) {
            convertedTime.add(timeArray[idx].substring(0, 2))
            continue
        }

        convertedTime.add(timeArray[idx])
    }


    var output = ""
    for (i in 0 until convertedTime.size) {

        if (i != convertedTime.size - 1) {
            output += "${convertedTime[i]}:"
        } else {
            output += convertedTime[i]
        }
    }

    return output

}

@Test
class TimeConversionTest {
    fun testTimeConversionInMorning() {
        val input = "07:05:45PM"
        val result = timeConversion(input)
        Assert.assertEquals(result, "19:05:45")
    }

    fun testTimeConversionAtMidnight() {
        val input = "12:40:22AM"
        val result = timeConversion(input)
        Assert.assertEquals(result, "00:40:22")
    }

    fun testTimeConversionInAfternoon() {
        val input = "12:45:54PM"
        val result = timeConversion(input)
        Assert.assertEquals(result, "12:45:54")
    }
}

//fun main(args: Array<String>) {
//    val scan = Scanner(System.`in`)
//    val s = scan.nextLine()
//    val result = timeConversion(s)
//    println(result)
//}
