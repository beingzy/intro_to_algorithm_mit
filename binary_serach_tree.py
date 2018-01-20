"""develop function to detect if a tree is BST

   BST has following properties:
   * The left subtree of a node contains only nodes
     with keys less than the node’s key.
   * The right subtree of a node contains only nodes
     with keys greater than the node’s key.
   * The left and right subtree each must also be a
     binary search tree.
"""
class Node():
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key


def print_inorder(root):
    if root:
        print_inorder(root.left)
        print(root.val)
        print_inorder(root.right)


def bst_search(root, key):
    if (root is None) or (root.val == key):
        return root

    if root.val < key:
        bst_search(root.right, key)

    return bst_search(root.left, key)


if __name__ == "__main__":
    root = Node(8)

    root.left = Node(3)
    root.left.left = Node(1)
    root.left.right = Node(6)
    root.left.right.left = Node(4)
    root.left.right.right = Node(7)

    root.right = Node(10)
    root.right.right = Node(14)
    root.right.right.left = Node(13)

    print('inorder traversal the Tree')
    print_inorder(root)

    print('search 4')
    print(bst_search(root, 4))
