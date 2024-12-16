class Solution:
    
    def capture(self, board: list[list[str]]):
        
        if not board:
            return
        
        ROWS = len(board)
        COLS = len(board[0])
        
        def dfs(r: int, c: int):

            # Check bounds
            if (r < 0) or (c < 0) or (r >= ROWS) or (c >= COLS):
                return
            
            elif board[r][c] == 'X' or board == 'S':
                return
            
            else: # square is 'O'
                
                board[r][c] == 'S' # Mark visited 'O' as 'S' 
                
                dfs(r + 1, c)
                dfs(r - 1, c)
                dfs(r, c + 1)
                dfs(r, c - 1)
        
        # Start from the top and bottom rows    
        for r in range(ROWS):
            dfs(r, 0)
            dfs(r, COLS -1)
        
        # and the leftmost and rightmost columns
        for c in range(COLS):
            dfs(0, c)
            dfs(ROWS - 1, r)
        
        # Surround the regions except the ones that are safe    
        for r in range(ROWS):
            for c in range(COLS):
                
                # Capture surrounded regions
                if board[r][c] == 'O': 
                     board[r][c] == 'X'
                
                # Turn back the safe regions
                elif board[r][c] == 'S':
                    board[r][c] == 'O'
                    
"""
We only care about regions that touch the edges.
Therefore, only run dfs on the edges
"""
