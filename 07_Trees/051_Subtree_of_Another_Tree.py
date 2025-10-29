def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
    
    # both nodes empty: matching
    if not p and not q:
        return True
    
    # only one node empty: not matching
    elif not p or not q:
        return False
    
    # values equal? we already checked that both nodes are not null
    if p.val != q.val:
        return False
    
    # are the children matching?
    else:
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
    
def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
    if not root:
        return False
    
    if self.isSameTree(root,subRoot):
        return True
    
    return self.isSubtree(root.left,subRoot) or self.isSubtree(root.right, subRoot)
    
