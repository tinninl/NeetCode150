def buildTree(self, preorder: list[int], inorder: list[int]) -> TreeNode:
    
    if inorder:
        i = inorder.index(preorder.pop(0))
        root = TreeNode(inorder[i])
        root.left = self.buildTree(preorder, inorder[0: i])
        root.right = self.buildTree(preorder, inorder[i + 1:]) 
    
    return root
    
    
    """
    3 9 20 15 7 
    9 3 15  20 7
    
    3 9 20 nul nul 15 7
    """
    