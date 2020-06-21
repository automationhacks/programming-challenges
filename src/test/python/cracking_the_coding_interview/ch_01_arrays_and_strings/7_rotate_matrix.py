"""
CTCI 6th edition: Chapter 1: Arrays and Strings, Problem 1.7

Rotate Matrix: Given an image represented by an NxN matrix, where each pixel in the image is 4 bytes, write a method to rotate the image by 90 degrees. (can you do this in place?
Hints: #51, #100

```python
    input_matrix = [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12],
        [13, 14, 15, 16]
    ]

    output_matrix = [
        [13, 9, 5, 1],
        [14, 10, 6, 2],
        [15, 11, 7, 3],
        [16, 12, 8, 4]
    ]
```

Hints:
Try thinking about it layer by layer. Can you rotate a specific layer?
Rotating a specific layer would just mean swapping the values in four arrays. If you were asked to swap the values in two arrays, could you do this? Can you then extend it to four arrays?

Official solution: https://github.com/careercup/CtCI-6th-Edition-Python/blob/master/Chapter1/7_Rotate%20Matrix/RotateMatrix.py
"""


def rotate_matrix(matrix):
    output = []
    length = len(matrix)

    for i in range(length):
        layer = []
        for j in range(length - 1, -1, -1):
            val = matrix[j][i]
            layer.append(val)
        output.append(layer)
    return output


def rotate_matrix_in_place(matrix):
    n = len(matrix)

    for layer in range(n // 2):
        first, last = layer, n - layer - 1

        print('')
        for i in range(first, last):
            print(f'Iteration {i}')
            # save top
            print(f"Setting top ({layer},{i})")
            top = matrix[layer][i]
            # left => top
            print(f"Left => top ({-i - 1},{layer})")
            matrix[layer][i] = matrix[-i - 1][layer]
            # bottom => left
            print(f"Bottom => left ({-layer - 1},{-i - 1})")
            matrix[-i - 1][layer] = matrix[-layer - 1][-i - 1]
            # right => bottom
            print(f"Right => bottom ({i},{-layer - 1})")
            matrix[-layer - 1][-i - 1] = matrix[i][-layer - 1]
            # top => right
            print(f"Top => right ({layer},{i})")
            matrix[i][-layer - 1] = top

    return matrix


def test_rotate_matrix():
    input_matrix = [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12],
        [13, 14, 15, 16]
    ]

    output_matrix = [
        [13, 9, 5, 1],
        [14, 10, 6, 2],
        [15, 11, 7, 3],
        [16, 12, 8, 4]
    ]

    assert rotate_matrix(input_matrix) == output_matrix
    assert rotate_matrix_in_place(input_matrix) == output_matrix
