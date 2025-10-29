
def search(nums: list[int]) -> int:
    
    l = 0
    r = len(nums) - 1
    res = nums[l]
    
    while l <= r:
        
        # If we found the sorted part
        if nums[l] <= nums[r]:
            res = nums[l]
            break
        
    
        m = (l + r) // 2
        
        if nums[m] < nums[r]: # mid element could be solution, include it in next search space
            r = m
            
        else:   # mid element cannot be solution, exclude it ( + 1)
            l = m + 1
            
    return res    
            