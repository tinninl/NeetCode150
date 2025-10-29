"""
72. Edit Distance

Given two strings word1 and word2, return the minimum number of operations 
required to convert word1 to word2.

You have the following three operations permitted on a word:

Insert a character
Delete a character
Replace a character

Example 1:

Input: word1 = "horse", word2 = "ros"
Output: 3
Explanation: 
horse -> rorse (replace 'h' with 'r')
rorse -> rose (remove 'r')
rose -> ros (remove 'e')
Example 2:

Input: word1 = "intention", word2 = "execution"
Output: 5
Explanation: 
intention -> inention (remove 't')
inention -> enention (replace 'i' with 'e')
enention -> exention (replace 'n' with 'x')
exention -> exection (replace 'n' with 'c')
exection -> execution (insert 'u')
 

Constraints:

0 <= word1.length, word2.length <= 500
word1 and word2 consist of lowercase English letters.
"""

"""
Step 1: What is the subproblem?
"""

"""
Step 2: What is the state?
Let dp[i][j] = the min ops needed to convert the first i chars of w1 into the first j chars of w2
"""

"""
Step 3: What is the recurrence relation?
If the chars match: dp[i][j] = dp[i - 1][j - 1] no operation needed
Else: we must either remove/insert/replace:
remove = dp[i - 1][j] + 1
insert = dp[i][j - 1] + 1
replace = dp[i-1][j-1] + 1
"""

class Solution:
    
    def minDistance(self, s: str, t: str) -> int:
        
        m = len(s)
        n = len(t)
        
        # Create a (m + 1) x (n + 1) DP table
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        
        ROWS, COLS = m + 1, n + 1
        
        # Base case 1: To convert t into the empty string s, we just need to delete
        for i in range(ROWS):
            dp[i][0] = i
        
        # Base case 2: To convert the empty string t into s, we just need to insert
        for j in range(COLS):
            dp[0][j] = j
            
        for i in range(1, ROWS):
            
            for j in range(1, COLS):
                
                # If characters match:
                if s[i - 1] == t[j - 1]:
                    
                    dp[i][j] = dp[i - 1][j - 1] # No additional operations needed
                    
                else:
                    
                    insert = dp[i][j - 1] + 1   # Pick the minimum number of operations
                    delete = dp[i - 1][j] + 1   
                    replace = dp[i - 1][j - 1] + 1
                    
                    dp[i][j] = min(delete, insert, replace)
                    
        return dp[-1][-1]
                    
        
                    