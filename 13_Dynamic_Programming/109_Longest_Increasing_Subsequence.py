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

class Solution:
    
    """
    Brute Force Solution: Generate every subsequence, 
    check if every single one is increasing, record length
    O(n^2)
    """
    def lengthOfLIS(self, nums: list[int]) -> int:
        
        n = len(nums)

        # Base case: The LIS = 1
        LIS = [1] * n
        
        for i in range(1, n):
            
            # Consider all subproblems
            for j in range(i):
                
                # Only consider subproblems where the prev element is less than curr element
                if nums[j] < nums[i]:
                    
                    # Update LIS
                    LIS[i] = max(LIS[i], LIS[j] + 1)
                           
        return max(LIS)
        