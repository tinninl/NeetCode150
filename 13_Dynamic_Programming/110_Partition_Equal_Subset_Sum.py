"""
416. Partition Equal Subset Sum

Given an integer array nums, return true if you can partition the array into two subsets 
such that the sum of the elements in both subsets is equal or false otherwise.

Example 1:

Input: nums = [1,5,11,5]
Output: true
Explanation: The array can be partitioned as [1, 5, 5] and [11].
Example 2:

Input: nums = [1,2,3,5]
Output: false
Explanation: The array cannot be partitioned into equal sum subsets.
 

Constraints:

1 <= nums.length <= 200
1 <= nums[i] <= 100
"""

class Solution:
    
    def canPartition(self, nums: list[int]) -> bool:
        
        s = sum(nums)

        if s % 2 == 1:
            return False
        
        target = s / 2
        
        n = len(nums)
       
        dp = [False] * (n + 1)
        dp[0] = True
                    
        for num in nums:
            
            for j in range(target, num - 1, -1):
                dp[j] = dp[j] or dp[j - num]
                
        return dp[target]
       
            