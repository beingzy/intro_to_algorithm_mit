"""three traversals

   * preorder:
     s1: visit root
     s2: preorder(left node)
     s3: preorder(ritght node)

   * inorder:
     s1: inorder(left node)
     s2: visit root
     s3: inorder(right node)

   * postorder:
     s1: left node postorder
     s2: right node postorder
     s3: visit root
"""

class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key


def print_inorder(root):
    if root:
        print_inorder(root.left)
        print(root.val)
        print_inorder(root.right)


def print_preorder(root):
    if root:
        print(root.val)
        print_preorder(root.left)
        print_preorder(root.right)


def print_postorder(root):
    if root:
        print_postorder(root.left)
        print_postorder(root.right)
        print(root.val)



if __name__ == '__main__':
   root = Node(1)
   root.left = Node(2)
   root.right = Node(3)
   root.left.left = Node(4)
   root.left.right = Node(5)

   print('postorder: [4, 2, 5, 2, 3]')
   print_inorder(root)

   print('postorder: [1, 2, 4, 5, 3]')
   print_preorder(root)

   print('postorder: [4, 5, 2, 3, 1]')
   print_postorder(root)
