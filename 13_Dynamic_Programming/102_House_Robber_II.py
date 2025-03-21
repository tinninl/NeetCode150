"""
Same as House Robber, except the first and last house are connected.
The houses form a circle
"""
def rob(nums: list[int]):
    
    n = len(nums)
        
    if n == 1:  # Check for length of 1 or else index error at dp[1]
        return nums[0]

    dp = [0] * n
        
    dp[0] = nums[0]
    dp[1] = max(nums[0], nums[1])
        
    for i in range(2, n):
        dp[i] = max(dp[i - 1], (dp[i - 2] + nums[i]))
            
    return dp[-1]



