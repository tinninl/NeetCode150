def invertTree(self, root: TreeNode) -> None:
    
    # Base case
    if not root:
        return None

    # Swap left and right children
    temp = root.left
    root.left = root.right
    root.right = temp
    
    self.invertTree(root.right)
    self.invertTree(root.left)
    
    return root