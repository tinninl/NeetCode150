class Solution:
    def longestIncreasingPath(self, matrix: list[list[int]]) -> int:
        
        rows, cols = len(matrix), len(matrix[0])
        
        dp = [[-1] * cols for _ in range(rows)] 
        
        directions = [(-1,0), (1,0), (0,-1), (0,1)]
        
        def dfs(i, j):
            
 

        
            
            if dp[i][j] != -1:
                return dp[i][j]
            
            max_len = 1  # At least the cell itself
            for di, dj in directions:
                ni, nj = i + di, j + dj
                if 0 <= ni < rows and 0 <= nj < cols and matrix[ni][nj] > matrix[i][j]:
                    max_len = max(max_len, 1 + dfs(ni, nj))
            
                    
            dp[i][j] = max_len
            
            return max_len
            
        max_path = 0
for i in range(rows):
    for j in range(cols):
        current_path = dfs(i, j)
        max_path = max(max_path, current_path)

return max_path
            
        