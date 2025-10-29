"""

Same as Climbing Stairs but this time there is a cost associated with every step.
Find the minimum cost to reach the top.

 

Example 1:

Input: cost = [10,15,20]
Output: 15
Explanation: You will start at index 1.
- Pay 15 and climb two steps to reach the top.
The total cost is 15.
Example 2:

Input: cost = [1,100,1,1,1,100,1,1,100,1]
Output: 6
Explanation: You will start at index 0.
- Pay 1 and climb two steps to reach index 2.
- Pay 1 and climb two steps to reach index 4.
- Pay 1 and climb two steps to reach index 6.
- Pay 1 and climb one step to reach index 7.
- Pay 1 and climb two steps to reach index 9.
- Pay 1 and climb one step to reach the top.
The total cost is 6.
 

Constraints:

2 <= cost.length <= 1000
0 <= cost[i] <= 999
"""

class Solution:
    """
    Step One: What is the subproblem?
    Similar to Climbing Stairs, the subproblem of step[n] is step[n - 1] and step[n - 2]
    
    Step Two: What is the state?
    Only one state, dp[i] = min cost to reach step i
    
    Step Three: What is the recurrence relation?
    step[n] = min(step[n - 1], step[n - 2]) + cost[n]
    
    Step Four: What is the base case?
    We always need to start on step[0] or step[1]
    
    """
    def minCostClimbingStairsMemo(self, cost: list[int]) -> int:
        
        n = len(cost)
    
        dp = [-1] * n
        
        def dfs(i):
            
            # Base cases
            if (i == 0) or (i == 0):
                return cost[i]
            
            # We reach a previously stored calculation
            if dp[i] != -1:
                return dp[i]
            
            dp[i] = min(dfs(i - 1), dfs(i - 2)) + cost[i]
            
            return dp[i]
        
        return dfs(n)
    
    def minCostClimbingStairsTab(self, cost: list[int]) -> int:
        
        n = len(cost)
        
        dp = [-1] * n
        
        dp[0], dp[1] = cost[0], cost[1]
        
        for i in range(2, n):
            
            dp[i] = min(dp[i - 1], dp[i - 2]) + cost[i]
            
        return min(dp[n - 1], dp[n - 2])
                                            

    
        
        
        