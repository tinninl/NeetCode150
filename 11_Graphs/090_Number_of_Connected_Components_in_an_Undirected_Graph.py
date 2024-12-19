
    
def countComponents (n: int, edges: list[list[int]]) -> int:
        
        neighbours = { i:[] for i in range(n)}
        
        for n1, n2 in edges:
            neighbours[n1].append(n2)
            neighbours[n2].append(n1)
            
        visit = set()
        
        groups = 0
        
        def dfs(node):
            
            # Check for loops
            if node in visit:
                return
            
            # Mark node as visited
            visit.add(node)
            
            # Visit each neighbour
            for n in neighbours[node]:
                
                dfs(n)
                
        for i in range(n):
            
            # Skip duplicate components
            if i in visit:
                continue
            
            dfs(i)
            
            groups += 1
            
        return groups        