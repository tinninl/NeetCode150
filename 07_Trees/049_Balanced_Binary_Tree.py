def isBalanced(root: TreeNode) -> bool:
    
    if not root:
        return True
    
    return dfsHeight(root) != - 1
    
def dfsHeight(root: TreeNode):
    
    if not root:
        return 0
    
    left = dfsHeight(root.left)
    right = dfsHeight(root.right)
    
    # If left or right subtree is not balanced, the entire tree is not balanced
    if (left == -1) or (right == -1):
        return -1
    
    if abs(left - right) > 1:
        return -1
    
    return max(left, right) + 1
    
    
    