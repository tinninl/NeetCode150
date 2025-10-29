import collections


def maxWindow(nums: list[int],k: int) -> list[int]:
    
    res = []
    
    l, r = 0, 0
    
    while r < len(nums):
        
        while q and nums[q[-1]] < nums[r]:
            q.pop()
            q.append(r)
            
        if 
            
    
    q= collections.deque()
    for i in range(nums):
        window = nums[i: i + k]