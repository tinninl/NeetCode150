def goodNode(root: TreeNode) -> int:
    
    def dfs(node, maxVal):
        
        if not root:
            return 0
        
        goodNodes
        
        if node.val < maxVal:
            goodNodes = 0
            
        else:
            goodNodes = 1
        
        maxVal = max(maxVal, node.val)
        
        goodNodes += dfs(root.left, maxVal)
        goodNodes += dfs(root.right, maxVal)
        
        return goodNodes
    
    return dfs(root, root.val)