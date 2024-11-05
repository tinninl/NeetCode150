def binarySearch(nums: list[int], target: int) -> int:
    
    l, r = 0, len(nums) - 1
    
    while l <= r:
        
        #mid = l + ((r - 1) // 2) find half the distance btwn r and l, add it to l, avoid overflow
        mid = (l + r) // 2
        
        if target < nums[mid]:
            r = mid - 1
            
        elif target > nums[mid]:
            l = mid + 1
            
        else:
            return mid
        
    return -1

nums = [4]
print(binarySearch(nums,4))