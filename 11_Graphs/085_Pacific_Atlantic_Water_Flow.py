def pacificAtlantic(self, heights: list[list[int]]) -> list[list[int]]:
    
    if (not heights) or (len(heights) == 0):
        return []
    
    ROWS, COLS = len(heights), len(heights[0])
    
    pac = [[False for _ in range(COLS)] for _ in range(ROWS)]
    atl = [[False for _ in range(COLS)] for _ in range(ROWS)]
    
    def dfs(r: int, c: int, visit: list[list[bool]], prevHeight: int):
        
        # Check bounds
        if r < 0 or c < 0 or r >= ROWS or c >= COLS:
            return
        
        # Have we already processed this square?
        if visit[r][c]:
            return
        
        height = heights[r][c]
        
        if height <= prevHeight:
            
            # Update visit set
            visit[r][c] = True     
            
            # Check neighbour cells
            dfs(r + 1, c, visit, height)
            dfs(r - 1, c, visit, height)
            dfs(r, c + 1, visit, height)
            dfs(r, c - 1, visit, height)
        
    # Top row - pac, bottom row - atl
    for c in range(COLS):
        dfs(0, c, pac, heights[0][c])
        dfs(ROWS - 1, c, atl, heights[ROWS - 1, c])
        
    # first col - pac, last col - atl
    for r in range(ROWS):
        
        dfs(r, 0, pac, heights[r][0])
        dfs(r, COLS - 1, atl, heights[r][COLS - 1])
    
    
    # Iterate matrix, if square is true for pac and atl, add to res
    res = []
    for r in range(ROWS):
        for c in range(COLS):
            if pac[r][c] and atl[r][c]:
                res.append([r, c])
    
    return res
            