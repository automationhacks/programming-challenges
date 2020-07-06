import sys

from python.cracking_the_coding_interview.ch_04_trees_graphs.minimum_bst import create_minimum_bst


def check_bst(node, min, max):
    if not node:
        return True

    less_than_node = not min and node.value <= min
    greater_than_node = (not max and node.value > max)
    if less_than_node or greater_than_node:
        return False
    
    if (not check_bst(node.left, min, node.value)) or (not check_bst(node.right, node.value, max)):
        return False
    
    return True


def test_tree_is_balanced():
    arr = list(range(1, 11))
    root = create_minimum_bst(arr, 0, len(arr) - 1)
    min = -sys.maxsize
    print(check_bst(root, min, root.value))
