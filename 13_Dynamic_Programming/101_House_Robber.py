"""
198. House Robber

You are a professional robber planning to rob houses along a street. 
Each house has a certain amount of money stashed, 
the only constraint stopping you from robbing each of them is that adjacent houses 
have security systems connected and it will automatically contact the police 
if two adjacent houses were broken into on the same night.

Given an integer array nums representing the amount of money of each house, 
the maximum amount of money you can rob tonight without alerting the police.

Example 1:

Input: nums = [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
Total amount you can rob = 1 + 3 = 4.
Example 2:

Input: nums = [2,7,9,3,1]
Output: 12
Explanation: Rob house 1 (money = 2), rob house 3 (money = 9) and rob house 5 (money = 1).
Total amount you can rob = 2 + 9 + 1 = 12.

Constraints:

1 <= nums.length <= 100
0 <= nums[i] <= 400
"""

"""
Step 1: What is the subproblem?
We need to know how much money we get from the last house

Step 2: What is the state?
Let dp[n] = the maximum profit we can make from house 0 to n

Step 3: What is the recurrence relation?
Two choices: 
Skip this house, dp[n] = dp[n - 1]
Rob this house dp[n], meaning we skip the previous (n-1) house dp[n] = dp[n - 2] + nums[n]

Step 4: Base Case(s)
One house, rob it nums[0]
Two house, rob the more valuable, max(nums[0], nums[1])

"""
class Solution:
    
    def robMemo(self, nums: list[int]) -> int:
        
        n = len(nums)
        dp = [-1] * n
        
        def dfs(i):
            
            if i == 0:
                return nums[0]
            if i == 1:
                return max(nums[0], nums[1])
            
            if dp[i] != -1:
                return dp[i]
            
            dp[i] = max(dfs(i - 1), dfs(i - 2) + nums[i])
            
            return dp[i]
        
        return dfs(n - 1)
            
        
        
    def robTab(self, nums: list[int]) -> int:
        
        n = len(nums)
        
        if n == 1:  # Check for length of 1 or else index error at dp[1]
            return nums[0]

        dp = [0] * n
        
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        
        for i in range(2, n):
            dp[i] = max(dp[i - 1], (dp[i - 2] + nums[i]))
            
        return dp[-1]