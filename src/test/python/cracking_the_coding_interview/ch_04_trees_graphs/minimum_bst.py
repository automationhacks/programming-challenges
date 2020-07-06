from python.cracking_the_coding_interview.ch_04_trees_graphs.tree_node import TreeNode


def create_minimum_bst(arr, start, end):
    if start > end:
        return ''

    mid = (start + end) // 2
    root = TreeNode(arr[mid])
    root.left = create_minimum_bst(arr, start, mid - 1)
    root.right = create_minimum_bst(arr, mid + 1, end)

    return root
