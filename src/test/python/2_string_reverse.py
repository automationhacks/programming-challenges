"""
Reverse a string or sentence
"""


def reverse_sentence(string):
    splitted = string.split()
    output = " ".join(splitted[::-1])
    print(output)


def reverse_string(string):
    print(string[::-1])


# This only traverses till half of the array, but the complexity is still O(n)
def reverse_array_num(array):
    length = len(array)
    for i in range(length // 2):
        other = length - i - 1
        temp = array[i]
        array[i] = array[other]
        array[other] = temp

    return array


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


def test_array_reverse():
    array = [4, 10, 5, 9, 7, 9]
    expected = [9, 7, 9, 5, 10, 4]
    assert reverse_array_num(array) == expected
