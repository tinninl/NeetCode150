"""
You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

 

Example 1:

Input: n = 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps
Example 2:

Input: n = 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step
 

Constraints:

1 <= n <= 45
"""

class Solution:
    
    """
    Step 1: What is the subproblem?
    To know the answer for 6 stairs, 
    we want to know the answer for 5 and 4 stairs.
    
    Step 2: What is the state?
    dp[n] = number of ways to climb to n steps
    
    Step 3: What is the recurrence relation?
    dp[n] = dp[n-1] + dp[n-2], just like fib seq
    
    Step 4: Base cases: 0 or 1 steps
    """
    
    def climbStairsMemo(self, n: int) -> int:
        
        dp = [0] * (n + 1)
        
        # Base cases
        dp[0] = 1
        dp[1] = 1
        
        def dfs(i):
            
            # We have reached a base case
            if i <= 1:
                return dp[i]
            
            # We have reached a previously stored calculation
            if dp[i] != 0:
                return dp[i]
            
            # Work backwards recursively
            dp[i] = dfs(i - 1) + dfs(i - 2)
            
            return dp[i]
        
        return dfs(n - 1)
    
    def climbStairsTab(self, n: int) -> int:
        
        dp = [0] * (n + 1)
        
        dp[0] = 0
        dp[1] = 1
        
        for i in range(2, len(dp)):
            dp[i] = dp[i - 1] + dp[i - 2]
        
        return dp[n]
    

            