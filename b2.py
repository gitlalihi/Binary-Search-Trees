#Python program to find the closest value to a given target value in a given non-empty Binary Search Tree (BST) of unique values.


class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def closest_value_in_bst(root, target):
    closest_value = float('inf')  # Initialize with positive infinity
    current_node = root

    while current_node is not None:
        
        if abs(current_node.value - target) < abs(closest_value - target):
            closest_value = current_node.value

        
        if target < current_node.value:
            current_node = current_node.left
        elif target > current_node.value:
            current_node = current_node.right
        else:
            
            return closest_value

    return closest_value

root = TreeNode(10)
root.left = TreeNode(5)
root.right = TreeNode(15)
root.left.left = TreeNode(2)
root.left.right = TreeNode(7)
root.right.left = TreeNode(12)
root.right.right = TreeNode(20)

target_value = 9
result = closest_value_in_bst(root, target_value)
print(f"The closest value to {target_value} in the BST is {result}")
