import sys

from python.cracking_the_coding_interview.ch_04_trees_graphs.minimum_bst import create_minimum_bst

MIN_SIZE = -sys.maxsize


def check_height(root):
    if not root:
        return -1

    left_height = check_height(root.left)
    if left_height == MIN_SIZE:
        return MIN_SIZE

    right_height = check_height(root.right)
    if right_height == MIN_SIZE:
        return MIN_SIZE

    height_diff = left_height - right_height

    if abs(height_diff) > 1:
        return MIN_SIZE
    else:
        return max(left_height, right_height) + 1


def is_balanced(root):
    return check_height(root) != MIN_SIZE


def test_tree_is_balanced():
    arr = list(range(1, 11))
    root = create_minimum_bst(arr, 0, len(arr) - 1)
    print(is_balanced(root))
