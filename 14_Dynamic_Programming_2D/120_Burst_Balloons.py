"""
312. Burst Balloons

You are given n balloons, indexed from 0 to n - 1. 
Each balloon is painted with a number on it represented by an array nums. 
You are asked to burst all the balloons.

If you burst the ith balloon, you will get nums[i - 1] * nums[i] * nums[i + 1] coins. 
If i - 1 or i + 1 goes out of bounds of the array, 
then treat it as if there is a balloon with a 1 painted on it.

Return the maximum coins you can collect by bursting the balloons wisely.
"""

"""
What is the subproblem?
Break it down into intervals, the smallest being length 2

What is the state? Let dp[l][r] = the maxCoins you can get from balloons[left] and balloons[right]

What is the RR?
In each interval, burst balloons[k] last. Then move to the left and right intervals, dp[left][k] and dp[k][right]

Base Case(s):
An interval of length 0 is impossible. An interval of length 1 is 0 (nothing is btwn left and right)

We fill the topright triangle of the matrix and the result is the topright corner cell (or the bottom left)
"""
class Solution:
    
    def maxCoins(self, nums: list[int]) -> int:
        
        nums = [1] + nums + [1]
        
        n = len(nums)
        dp = [[[0] * n] for _ in range(n)]
        
        
        for length in (2, n):   # Check every interval from length 2 to length n
            
            for left in range(0, n - length):
                
                right = left + length
                
                for k in range(left + 1, right):
                    coins = nums[left] * nums[k] * nums[right]
                    total = coins + dp[left][k] + dp[k][right]
                    dp[left][right] = max(dp[left][right], total)
                    
        return dp[0][-1]
    
"""
We fill out dp[0][2], dp[1][3], dp[2][4], etc for interval of length 2
Then [0][3],[1][3],[2][4] for length 3
At the end, the last one to fill is [0][n-1]
"""
        