"""
    Flatten a list having multiple nested lists
    E.g. [1, [1, 2], [2, [3, 4]]]

    Write test cases to test your functions.

    Solution from: https://codereview.stackexchange.com/questions/178600/flatten-an-array-of-integers-in-python?newsletter=1&nlcode=571243%7c9f95
"""


def flatten_list(lst):
    flattened = []

    for item in lst:
        if isinstance(item, list):
            flat_list = flatten_list(item)
            flattened.extend(flat_list)
        else:
            flattened.append(item)
    return flattened


def flatten_list_using_generators(lst):
    for element in lst:
        if isinstance(element, list):
            yield from flatten_list_using_generators(element)
        elif isinstance(element, int):
            yield element
        else:
            raise TypeError('Unsupported type ({})'.format(type(element).__name__))


if __name__ == '__main__':
    nested = [1, [1, 2], [2, [3, 4]]]

    print(flatten_list(nested))
    print(list(flatten_list_using_generators(nested)))
