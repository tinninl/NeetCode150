def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
    
    if not node:
        return None
    
    # A hashmap mapping original nodes to their copies
    oldToNew = {}
    
    def dfs(node):
        
        if node in oldToNew:
            return oldToNew[node]
        
        copy = Node(node.val)
        oldToNew[node] = copy
        
        for n in node.neighbors:
             copy.neighbors.append(dfs(n))
             
        return copy
      
    return dfs(node)