def invertTree(root: TreeNode) -> None:
    
    # Base case
    if not root:
        return None

    # Swap child nodes
    temp = root.left
    root.left = root.right
    root.right = temp
    
    # Call function on child nodes
    invertTree(root.right)
    invertTree(root.left)
    
    return root