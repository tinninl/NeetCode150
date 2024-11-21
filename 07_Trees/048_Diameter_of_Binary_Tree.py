
diameter = 0

def diameter(root: TreeNode) -> int:
    
    if not root: 
        return 0
    
    maxDepth(root)
    
    return diameter

def maxDepth(root: TreeNode) -> int:
    
    # Base case
    if not root:
        return 0
    
    # Find the max depth of left and right children
    left = maxDepth(root.left)
    right = maxDepth(root.right)
    
    # Update diameter
    diameter = max(diameter, left + right)
    
    return 1 + max(left, right)