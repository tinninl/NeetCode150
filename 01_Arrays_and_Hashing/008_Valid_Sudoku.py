class Solution:
    
    def isValidSudoku(board: list[list[str]]) -> bool:  
          
        for i in range(9):
            
            rowSet = set()
            colSet = set()
            blockSet = set()
            
            for j in range(9):
                
                s = board[i][j]
                
                if (s != "."):            
                    if s in rowSet:
                        return False
                    else:
                        rowSet.add(s)
                    
                s = board[j][i]
                
                if s != ".":
                    
                
                    if s in colSet:
                        return False
                    else:
                        colSet.add(s)
                        
                s = board[((i // 3) * 3) + (j // 3)][(j % 3) + ((i % 3) * 3)]
                
                if s != ".":
                    
                
                    if s in blockSet:
                        return False
                    else:
                        blockSet.add(s)
                        
                        
        return True
    