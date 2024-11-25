def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        if not root:
            return []
        
        res = []

        q = collections.deque()

        q.append(root)

        while q:
            
            n = len(q)
            level = [] 
            
            for i in range(n):
                
                node = q.popleft()
                
                if node:
                    level.append(node.val)
                    q.append(node.left)
                    q.append(node.right)
                    
            if level:
                res.append(level)

        return res
    