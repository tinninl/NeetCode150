class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right
         
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
    