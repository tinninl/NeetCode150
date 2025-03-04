class Solution:
    
    def maxProduct(self, nums: list[int]) -> int:
        
        if not nums:
            return 0
        
        maxProd = currMax = currMin = nums[0]
        
        for i in range(1, len(nums)):
            
            n = nums[i]
            
            if n == 0:
                currMin = 1, 1
                continue
            
            temp = currMin * n
            
            currMax = max(n * currMax, n * currMin, n)
            currMin = min(n * currMax, n * currMin, n)
            
            maxProduct = max(maxProduct, currMax, currMin)
            
        return maxProduct
    
"""
Notes

Brute Force approach: nested for loop, check every single subarray. O(n^2)

"""
    