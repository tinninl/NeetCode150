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
    
    def climbStairs(self, n: int) -> int:
        
        if n <= 2:
            return n 
        
        cache = [0] * (n + 1)
        
        cache[1] = 1
        cache[2] = 2
        
        for i in range(3, n + 1):
            
            cache[i] = cache[i - 1] + cache[i - 2]
            
        return cache[-1]
    
"""
Notes:
fib seq starting at 1 and 2
use cache
return last step
dp: use the prev results to calculate the next result
"""
            