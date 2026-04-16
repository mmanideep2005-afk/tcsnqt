from collections import deque

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def count_nodes(root):
    if root is None:
        return 0
    return 1 + count_nodes(root.left) + count_nodes(root.right)


def count_leaves(root):
    if root is None:
        return 0
    if root.left is None and root.right is None:
        return 1
    return count_leaves(root.left) + count_leaves(root.right)


def height(root):
    if root is None:
        return 0
    return 1 + max(height(root.left), height(root.right))


def level_order(root):
    if not root:
        return

    q = deque([root])

    while q:
        node = q.popleft()
        print(node.data, end=" ")

        if node.left:
            q.append(node.left)
        if node.right:
            q.append(node.right)


def main():
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)

    print("Total nodes:", count_nodes(root))
    print("Height:", height(root))
    print("Leaf Nodes:", count_leaves(root))

    print("Level Order:")
    level_order(root)

main()