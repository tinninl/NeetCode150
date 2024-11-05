def search(nums: list[int], target: int) -> int:
    
    l, r = 0, len(nums) - 1
    
    while l <= r:
        
        m = l + ((r - l) // 2)
        
        if nums[m] == target:
            return m
        
        if nums[l] <= nums[m]: # left side is sorted
            
            if nums[l] < target <= nums[m]: # target is in lefthalf
                r = m - 1
                
            else:
                l = m + 1
                
        else: # right side is sorted
        
            if nums[m] < target <= nums[r]: # target is in right side
                l = m + 1
                
            else:
                r = m - 1
                
    return -1

nums = [4,3]
print(search(nums,3))