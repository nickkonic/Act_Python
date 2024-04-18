class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = self.right = None

def insert(root, key):
    if root is None:
        return TreeNode(key)
    if root.data < key:
        root.right = insert(root.right, key)
    else:
        root.left = insert(root.left, key)
    return root

def pre_order_traversal(root):
    if root:
        print(root.data, end=' ')
        pre_order_traversal(root.left)
        pre_order_traversal(root.right)

if __name__ == "__main__":
    root = None

    print("Enter 10 numbers:")
    for _ in range(10):
        num = int(input())
        root = insert(root, num)

    print("\nPre-order traversal:")
    pre_order_traversal(root)
