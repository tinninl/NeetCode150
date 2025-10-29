def validateBST(self,root: TreeNode) -> bool:
    
    # Base case
    if not root: 
        return True
    
    # Does this node have a valid left child?
    if root.left and root.left.val > root.val:
        return False
    
    # A valid right child?
    if root.right and root.right.val < root.val:
        return False
    
    # Validate left and right children
    return self.validateBST(root.left) and self.validateBST(root.right)
    
    
        