"""
Given a string as 'This is really a test if there are duplicates'
Find if there are duplicate chars with their index
"""


def find_duplicate_chars(strng):
    """
    Logic:
    enumerate(string) returns a iterable with tuple of pos and char of string
    :param strng: input string
    :return: dict with key as char and value as list of all indexes
    """
    mapping = {}

    for pos, char in enumerate(strng.lower()):
        if char in mapping.keys():
            mapping[char].append(str(pos))
        else:
            mapping[char] = []
    return mapping


def print_sorted_dict(dct):
    for k, v in sorted(dct.items()):
        if v:
            print('{} {}'.format(k, v))


if __name__ == '__main__':
    dct = find_duplicate_chars('This is really a test if there are duplicates')
    print_sorted_dict(dct)
