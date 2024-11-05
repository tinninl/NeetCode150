"""
Look at the negative numbers only, and find two numbers that sum to it
"""
def threeSum(nums: list[int], target: int) -> list[list[int]]:
    
    res = []
    
    nums.sort()
    
    for i, n in enumerate(nums):
        
        if (n > 0): # skip positive values
            break
        
        if (i > 0 and n == nums[i - 1]):    # skip duplicate values
            continue
        
        l, r = i + 1, len(nums) - 1
        
        while (l < r):
            
            threeSum = n + nums[l] + nums[r]
            
            if (threeSum < 0):
                l += 1
                
            elif (threeSum > 0):
                r -= 1
                
            else:
                
                res.append[n, nums[l], nums[r]]
                
                l += 1
                r -= 1
                
                while l < r and nums[l] == nums[l - 1] : # skip duplicate solutions
                    l += 1
    
    return res
            