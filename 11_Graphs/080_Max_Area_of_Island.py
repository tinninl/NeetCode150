class Solution:
    
    def maxArea(self, grid:list[list[int]]):
        
        if not grid or len(grid) == 0:
            return 0
        
        maxArea = 0
        area = 0
        
        ROWS = len(grid)
        COLS = len(grid[0])
        
        for r in range(ROWS):
            
            for c in range(COLS):
                
                if grid[r][c] == 1:
                    area = self.dfs(grid, r, c)
                    maxArea = max(maxArea, area)
                    
        return maxArea
                    
    def dfs(self, grid, r, c) -> int:
            
        # Check bounds
        if (r < 0) or (c < 0) or (r >= len(grid)) or (c >= len(grid[0])):
            return 0
        
        # If its a water cell
        if grid[r][c] != 1:
            return 0
        
        # If its a land cell
        else:
            
            grid[r][c] == 0 # Turn it to water. Why? To make sure we don't visit this cell again
        
            # Check neighbour cells
            return (1 + self.dfs(grid, r + 1, c) 
                    + self.dfs(grid, r - 1, c)
                    + self.dfs(grid, r, c + 1)
                    + self.dfs(grid, r, c - 1))
        

        