"""
300 Longest Increasing Subsequence

Given an integer array nums, return the length of the longest strictly increasing subsequence.

Example 1:

Input: nums = [10,9,2,5,3,7,101,18]
Output: 4
Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4.
Example 2:

Input: nums = [0,1,0,3,2,3]
Output: 4
Example 3:

Input: nums = [7,7,7,7,7,7,7]
Output: 1
 

Constraints:

1 <= nums.length <= 2500
-104 <= nums[i] <= 104
 

Follow up: Can you come up with an algorithm that runs in O(n log(n)) time complexity?
"""

"""
Step One: What is the subproblem?
"""
class Solution:

    def lengthOfLIS(self, nums: list[int]) -> int:
        
        n = len(nums)

        # Base case: The LIS = 1
        dp = [1] * n
        
        for end in range(1, n):
            
            # Consider all subproblems
            for start in range(end):
                
                # Only consider subproblems where the prev element is less than curr element
                if nums[start] < nums[end]:
                    
                    # Update LIS
                    dp[end] = max(dp[end], dp[start] + 1)
                           
        return max(dp)

    def lengthOfLIS(self, nums: list[int]) -> int:
        res= 1
        n = len(nums)
        
        memo = [-1] * n
        memo[0] = 1
        
        def dfs(i):
            
            if i == 0:
                return 1
            
            if memo[i] != -1:
                return memo[i]
            maxLength = 1
            for j in range(i):
                if nums[j] < nums[i]:
                    maxLength = max(maxLength, 1 + dfs(j))
            
            memo[i] = maxLength 
            return maxLength

        for i in range(n):
            res = max(res, dfs(i))
        return res
            
            