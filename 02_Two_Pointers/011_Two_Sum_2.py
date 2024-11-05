def twoSum2(nums: list[int], target: int) -> list[int]:
    
    l, r = 0, len(nums) - 1
    
    while (l < r):
        
        sum = nums[l] + nums[r]
        
        if (sum < target):
            l += 1
            
        elif (sum > target):
            r -= 1
            
        else:
            return [l + 1, r + 1] # question states array is 1-indexed, so we must add 1
        
    return [-1,-1]