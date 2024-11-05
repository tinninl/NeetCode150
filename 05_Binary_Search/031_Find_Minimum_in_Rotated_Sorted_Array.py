
def search(nums: list[int]) -> int:
    
    l = 0
    r = len(nums) - 1
    res = nums[l]
    
    while l <= r:
        
        if nums[l] <= nums[r]: # <= in case search array is size = 1 (l = r)
            res = nums[l]
            break
        
        m = (l + r) // 2
        print("left:", l, " right:", r, "mid:", m)
        
        if nums[m] < nums[r]: # mid element could be solution, include it
            r = m
            
        else:   # mid element cannot be solution, exclude it
            l = m + 1
            
    return res
        
nums = [3,4,0,1,2]

print(search(nums))      
            