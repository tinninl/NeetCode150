import collections

def rottingOranges(self, grid: list[list[int]]) -> int:
    
    if not grid or len(grid) == 0:
        return -1
    
    ROWS = len(grid)   
    COLS = len(grid[0])
    
    fresh = 0
    rotten = collections.deque()
    
    # Count all fresh oranges and add all rotten oranges to the queue
    for r in range(ROWS):    
        for c in range(COLS):
            
            # If orange is rotten
            if grid[r][c] == 2:
                rotten.append((r, c))
            
            # If orange is fresh
            elif grid[r][c] == 1:
                fresh += 1
                
    time = 0
    dirs = [[0, 1], [0,-1], [1, 0], [-1, 0]]
    
    # Process every rotten orange in bfs
    while rotten and fresh > 0:
        
        n = len(rotten)
        
        for _ in range(n):
            
            r, c = rotten.popleft()
            
            for dr, dc in dirs:
                
                r += dr
                c += dc

                # Check bounds
                if (r < 0) or (c < 0) or (r >= ROWS) or (c >= COLS):
                    continue
                
                # If adj orange is fresh, 
                if grid[r][c] == 1:
                    
                    grid[r][c] == 2     # it becomes rotten
                    
                    rotten.append((r, c)) # add the new rotten orange to the queue
                    
                    fresh -= 1  # update num of fresh oranges
                

        time +=1
            
    if fresh == 0:
        return time
    else:
        return -1
      
        
            
            
            
                
                
                
    
                
    