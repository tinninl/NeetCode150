class Solution:
    
    def maxProduct(self, nums: list[int]) -> int:
        
        if not nums:
            return 0
        
        # Base cases
        maxProd = nums[0]
        minProd = nums[0]
        res = nums[0]
        
        for i in range(1, len(nums)):
            
            # Upon reaching a neg, swap max and mid prod
            if nums[i] < 0:
                temp = maxProd
                maxProd = minProd
                minProd = temp
                
            maxProd = max(nums[i], maxProd * nums[i])
            minProd = min(nums[i], minProd * nums[i])
            
            res = max(res, maxProd)
        
        return res
        
    
"""
Notes

Brute Force approach: nested for loop, check every single subarray. O(n^2)

"""
    