#Python program to check whether a given binary tree is a valid binary search tree (BST) or not.
class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def is_valid_bst(root, min_val=float('-inf'), max_val=float('inf')):
    if root is None:
        return True

    if not (min_val < root.value < max_val):
        return False

    return (is_valid_bst(root.left, min_val, root.value) and
            is_valid_bst(root.right, root.value, max_val))


root = TreeNode(2)
root.left = TreeNode(3)
root.right = TreeNode(1)

result = is_valid_bst(root)
print("Is the tree a valid BST?", result)
