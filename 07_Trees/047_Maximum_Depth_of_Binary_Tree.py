def maxDepth(root: TreeNode) -> int:
    
    # Base case
    if not root:
        return 0
    
    # Find the max depth of left and right children
    left = maxDepth(root.left)
    right = maxDepth(root.right)
    
    return 1 + max(left, right)