def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
    
    res = []
    
    levels = self.levelOrder(root)
    
    for level in levels:
        res.append(level[-1]) # Add the rightmost node of each level
        
    return res
           
def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        res = []
        if not root:
            return []

        q = collections.deque()

        q.append(root)

        while q:
            qLen = len(q)
            level = []
            for i in range(qLen):
                node = q.popleft()
                if node:
                    level.append(node.val)
                    q.append(node.left)
                    q.append(node.right)
            if level:
                res.append(level)

        return res    