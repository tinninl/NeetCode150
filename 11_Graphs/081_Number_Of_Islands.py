class Solution:
    def numIslands(self, grid: list[list[str]]) -> int:
        
        # Base case: empty grid
        if not grid:
            return 0
        
        ROWS = len(grid)
        COLS = len(grid[0])
        
        numIslands = 0
        
        # Check every square for an island
        
        for r in range(ROWS):
            
            for c in range(COLS):
                
                if grid[r][c] == "1":
                    
                    self.dfs(grid, r, c) # Call dfs to find all connecting land squares
                    numIslands += 1
        
        return numIslands
    
    def dfs(self, grid: list[list[int]], r: int, c: c):
        
        # If out of bounds, end
        if (r < 0) or (c < 0) or (r >= len(grid)) or (c >= len(grid[0])):
            return
        
        # If not a land piece, end
        elif grid[r][c] != "1":
            return
        
        # Turn the land square into a water square (or anything else)
        grid[r][c] = "0"
        
        # Run dfs on all four adjacent squares
        self.dfs(grid, r + 1, c)
        self.dfs(grid, r - 1, c)
        self.dfs(grid, r, c + 1)
        self.dfs(grid, r, c - 1)
        
        
        
                    
        
        