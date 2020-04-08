"""
Reverse a string or sentence
"""


def reverse_sentence(string):
    splitted = string.split()
    output = " ".join(splitted[::-1])
    print(output)


def reverse_string(string):
    print(string[::-1])


def rreverse(string):
    """
    Reverse string using recursion
    :param string:
    :return:
    """
    if string == '':
        return string  # If empty string is passed, return it
    else:
        # Logic:
        # 1. Get last char of string using string[-1]
        # 2. Call the function again with the reduced chars, 
        # i.e [:-1] is equivalent to [0:-1]
        # and the last limit is ignored
        # 3. Concat it
        return string[-1] + rreverse(string[:-1])


if __name__ == '__main__':
    string = "This is a car"

    reverse_sentence(string)
    reverse_string(string)
    print(rreverse('ReverseThis'))
