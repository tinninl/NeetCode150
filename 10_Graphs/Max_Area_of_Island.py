class Solution:
    def maxArea(self, grid:list[list[int]]):
        
        if not grid:
            return 0
        
        maxArea = 0
        area = 0
        
        rows = len(grid)
        cols = len(grid[0])
        
        for r in range(rows):
            
            for c in range(cols):
                
                if grid[r][c] == 1:
                    area = self.dfs(grid, r, c*)
                    maxArea = max(maxArea, area)
                    
        return maxArea
                    
    def dfs(self, grid, r, c) -> int:
            
        if r < 0 or c < 0 or r >= len(grid) or c >= len(grid[0]):
            return 0
        
        if grid[r][c] != 1:
            return 0
        
        grid[r][c] == 0
        
        return (1 + self.dfs(grid, r + 1, c) 
                  + self.dfs(grid, r - 1, c)
                  + self.dfs(grid, r, c + 1)
                  + self.dfs(grid, r, c - 1))
        

        