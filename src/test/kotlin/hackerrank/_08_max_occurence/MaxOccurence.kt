package hackerrank._08_max_occurence

/**
 * Given a string, find out the character which occurs most, in case there is a tie,
 * ensure the element that comes first should be the character
 * Ex: "helloworld"
 * Expected: l (since it comes 3 times)
 */

fun maximumOccurringCharacter(text: String): Char {
    val charCountMapping = linkedMapOf<Char, Int>()

    for (eachCharacter in text) {
        charCountMapping.incrementCharCountFor(eachCharacter)
    }

    return getCharWithMaxValue(charCountMapping)
}

fun HashMap<Char, Int>.incrementCharCountFor(key: Char): HashMap<Char, Int> {
    val value = this.getOrDefault(key, 0)
    this[key] = value + 1
    return this
}

private fun getCharWithMaxValue(charCountMapping: LinkedHashMap<Char, Int>) =
    charCountMapping.maxBy { it.value }?.key!!

fun main() {
    val string = "helloworld"
    val result = maximumOccurringCharacter(string)
    print(result)
}