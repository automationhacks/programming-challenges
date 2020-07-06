class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def list_of_depths_bfs(root):
    if not root:
        return

    queue = [root]

    while len(queue) > 0:
        node = queue.pop(0)
        print(node.value)

        if node.left:
            queue.append(node.left)

        if node.right:
            queue.append(node.right)


def test_list_of_depths():
    root = TreeNode(4)
    root.left = TreeNode(5)
    root.right = TreeNode(6)
    root.left.left = TreeNode(7)
    root.left.right = TreeNode(8)
    root.right.left = TreeNode(9)
    root.right.right = TreeNode(10)

    list_of_depths_bfs(root)
