"""
URLify: Write a method to replace all spaces in a string with '%20:
You may assume that the string has sufficient space at the end to
hold the additional characters, and that you are given the
"true" length of the string.
(Note: If implementing in Java, please use a character array so that
you can perform this operation in place.)

EXAMPLE

Input: "Mr John Smith    ", 13
Output: "Mr%20John%20Smith"

Solution:
1. Count no of spaces
2. Start from end and keep on replacing the chars one by one
3. If you see a space then replace %20 and then jump

"""


def urlify(chars, length):
    if not chars:
        return ''

    space_count = 0
    for i in range(length):
        if chars[i] == ' ':
            space_count += 1

    index = length + 2 * space_count - 1
    i = length - 1

    while i >= 0:
        current_char = chars[i]
        if current_char != ' ':
            chars[index] = current_char
            index -= 1
        else:
            chars[index] = '0'
            chars[index - 1] = '2'
            chars[index - 2] = '%'
            index -= 3
        i -= 1

    return ''.join(chars)


def test_urlify():
    assert (urlify(list('Mr John Smith    '), 13)) == 'Mr%20John%20Smith'
