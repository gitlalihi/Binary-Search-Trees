#Python program to find the kth smallest element in a given binary search tree.
class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def kth_smallest_element(root, k):
    
    def inorder_traversal(node):
        nonlocal k, result

        if node is None or k == 0:
            return
        inorder_traversal(node.left)
        k = k-1 
        if k == 0:
            result = node.value
            return
        inorder_traversal(node.right)
    result = None
    inorder_traversal(root)
    return result


root = TreeNode(3)
root.left = TreeNode(1)
root.right = TreeNode(4)
root.left.leftright = TreeNode(2)

k = 2
result = kth_smallest_element(root, k)
print(f"The {k}th smallest element in the BST is: {result}")
