class Solution:
    
    def hi(self, n: int, edges: list[list[int]]) -> int:
        
        neighbours = { i:[] for i in range(n)}
        
        for n1, n2 in edges:
            neighbours[n1].append(n2)
            neighbours[n2].append(n1)
            
        visit = set()
        
        def dfs(curr, prev):
            
            if curr in visit:
                return
            
            visit.add(curr)
            
            for n in neighbours[curr]:
                dfs
        