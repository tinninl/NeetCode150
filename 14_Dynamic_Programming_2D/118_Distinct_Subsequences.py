class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        
        ROWS, COLS = len(s), len(t)
        
        dp = [[0] * (COLS + 1) for _ in range(ROWS + 1)]
        
        # Base case: t is an empty string
        for i in range(ROWS + 1):
            dp[i][0] = 1
            
        for i in range(ROWS + 1):
            
            for j in range(COLS + 1):
                
                if s[i - 1] == t[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j]
                    
                else:
                    dp[i][j] = dp[i - 1][j]
                    
        return dp[ROWS][COLS]
                