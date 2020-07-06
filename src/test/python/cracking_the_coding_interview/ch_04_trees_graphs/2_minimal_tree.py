from python.cracking_the_coding_interview.ch_04_trees_graphs.minimum_bst import create_minimum_bst


def test_minimum_bst():
    arr = list(range(0, 10))
    node = create_minimum_bst(arr, 0, len(arr) - 1)

    print()
    print(arr)
    print(node)
