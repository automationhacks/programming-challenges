"""
Sort a list content
[2, 4, 7, 5, 8, 3] or [0, 1, 0, 1, 1, 0]
Note: Below is basically bubble sort algorithm
"""


def sort_list(numbers):
    i = 0
    while i < len(numbers):
        j = i + 1
        while j < len(numbers):
            if numbers[i] > numbers[j]:
                # Exchange nos if outside loop no is > inner loop
                temp = numbers[i]
                numbers[i] = numbers[j]
                numbers[j] = temp
            j += 1
        i += 1
    return numbers


if __name__ == '__main__':
    print(sort_list([2, 4, 7, 5, 8, 3]))
    print(sort_list([0, 1, 0, 1, 1, 0]))
