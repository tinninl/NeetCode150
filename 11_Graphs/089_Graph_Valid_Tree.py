class Solution:

    def validTree(self, n: int, edges: list[list[int]]) -> bool:
        
        # Create an adjacency list (hashmap)
        # mapping nodes to its neighbours
        neighbours = { i:[] for i in range(n)}
        
        for n1, n2 in edges:
            neighbours[n1].append(n2)
            neighbours[n2].append(n1)
            
        visit = set()
        
        def dfs(curr, prev):
            
            # Check for loop
            if curr in visit:
                return False
            
            visit.add(curr)
            
            for n in neighbours[curr]:
                
                if n == prev:
                    continue
                
                if not dfs(n, curr):
                    return False
                
            return True
        
        # If no loop was detected and every node is connected, its valid
        if dfs(0, -1) and len(visit) == n:
            return True
        
        else:
            return False
            
            