def rob(nums: list[int]):
    
    n = len(nums)
    
    cache = [0] * n
    
    cache[0] = nums[0]
    cache[1] = nums[1]
    
    for i in range(2, n):
        
        cache[i] = max(cache[i - 1], cache[i - 2] + nums[i])
        
    return max(cache[-1] - nums[0], cache[-2])

nums = [2,7,9,3,1]

print(rob(nums))

"""
since last house is connected to first house, account for that in return stmnt
"""