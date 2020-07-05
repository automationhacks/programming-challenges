class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def create_minimum_bst(arr, start, end):
    if start > end:
        return ''

    mid = (start + end) // 2
    root = TreeNode(arr[mid])
    root.left = create_minimum_bst(arr, start, mid - 1)
    root.right = create_minimum_bst(arr, mid + 1, end)

    return root


def test_minimum_bst():
    arr = list(range(0, 10))
    node = create_minimum_bst(arr, 0, len(arr) - 1)

    print()
    print(arr)
    print(node)
