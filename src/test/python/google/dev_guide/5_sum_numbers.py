"""
Given a string, return the sum of the numbers appearing in the string, ignoring all other characters.
A number is a series of 1 or more digit chars in a row. (Note: Character.isDigit(char)
tests if a char is one of the chars '0', '1', .. '9'. Integer.parseInt(string) converts a string to an int.)

sumNumbers("abc123xyz") → 123
sumNumbers("aa11b33") → 44
sumNumbers("7 11") → 18
"""


def test_sum_numbers_with_one_number():
    assert sum_numbers('abc123xyz') == 123


def test_sum_numbers_at_end():
    assert sum_numbers('aa11b33') == 44


def test_sum_numbers_at_beggining():
    assert sum_numbers('11aa11b33') == 55


def test_sum_numbers_with_only_numbers():
    assert sum_numbers('7 11') == 18


def sum_numbers(string):
    total = 0
    digit = ''

    idx = 0
    while idx < len(string):
        char = string[idx]

        if char.isdigit():
            digit += char

        if not char.isdigit() and digit:
            total += int(digit)
            digit = ''

        idx += 1

    # Digit at the end case
    if digit:
        total += int(digit)

    return total
