"""
Given an input string s and a pattern p, implement regular expression 
matching with support for '.' and '*' where:

'.' Matches any single character.​​​​
'*' Matches zero or more of the preceding element.
The matching should cover the entire input string (not partial).
"""

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        
        
        dp = [[False] * (len(p) + 1) for _ in range((len(s) + 1))]
        
        dp[0][0] = True
        
        ROWS = len(dp)
        COLS = len(dp[0])
        
        for i in range(ROWS):
            for j in range(COLS):
                
                match = i >= len(s) and p[j] in {s[i], "."}
                
                if j -1 >= 0 and p[j - 1] == "*":
                    dp[i][j] = dp[i][j - 2] 
                    
                    
                
                    
                
        