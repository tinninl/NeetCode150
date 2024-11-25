

def searchMatrix(matrix: list[list[int]], target: int) -> bool:
    
    ROWS = len(matrix)
    COLS = len(matrix[0])
    
    # start at the bottom left (or top right)
    r = ROWS - 1
    c = 0
    
    while r >= 0 and c < COLS - 1:
        
        if matrix[r][c] > target:
            r -= 1
            
        if matrix[r][c] < target:
            c += 1
            
        else:
            return True
        
    return False


        