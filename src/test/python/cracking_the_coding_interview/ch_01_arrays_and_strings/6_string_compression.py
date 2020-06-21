"""
CTCI 6th edition: Chapter 1: Arrays and Strings, Problem 1.6

String Compression: Implement a method to perform basic string compression using the counts of repeated characters.
For example, the string aabcccccaaa would become a2b1c5a3. If the "compressed" string would not become smaller than
the original string, your method should return the original string.
You can assume the string has only uppercase and lowercase letters (a - z).

Hints: #92, # 110

- Do the easy thing first. Compress the string, then compare the lengths.
- Be careful that you aren't repeatedly concatenating strings together. This can be very inefficient.
"""

# Official solution
# https://github.com/careercup/CtCI-6th-Edition-Python/blob/master/Chapter1/6_String%20Compression/StringCompression.py


# O(n)
def compress_string(string):
    previous_char = ''
    previous_char_count = 0
    output = []

    for current_char in string:
        if current_char != previous_char:
            if previous_char:
                compressed = f'{previous_char}{previous_char_count}'
                output.append(compressed)

            previous_char = current_char
            previous_char_count = 1
        else:
            previous_char_count += 1

    output.append(f'{previous_char}{previous_char_count}')

    return min(string, ''.join(output), key=len)


def test_compress_string():
    test_data = [
        ('aabcccccaaa', 'a2b1c5a3'),  # Base
        ('aab', 'aab'),  # Output > Input
        ('aabcAAcccBBcaaaaaaaaaaaa', "a2b1c1A2c3B2c1a12")  # lower/upper mixed
    ]

    for string, output in test_data:
        assert compress_string(string) == output
