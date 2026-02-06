# Create two arrays, left and right, to track the products before and after self.
# Multiply the left and right arrays togther to create the resultant array

class Solution:
    
    def productExceptSelf(nums: list[int]) -> list[int]:
        
        n = len(nums)
        
        left = [1] * n
        right = [1] * n
        res = [1] * n
        
        # Fill left array
        for i in range(1, n):
            left[i] = left[i - 1] * nums[i - 1]
        
        # Fill right array
        for i in range(n - 2, -1, -1):
            right[i] = right[i + 1] * nums[i + 1]
        
        # Fill resultant array
        for i in range(n):
            res[i] = left[i] * right[i]
        
        return res
