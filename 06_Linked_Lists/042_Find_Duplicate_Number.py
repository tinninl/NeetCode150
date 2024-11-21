def findDuplicate(self, nums: List[int]) -> int:
    
    slow = nums[0]
    fast = nums[nums[0]]
    
    while slow != fast:
        slow = nums[slow]
        fast = nums[nums[fast]]
        
    fast = 0
    
    while slow != fast:
        fast = nums[fast]
        slow = nums[slow]
        
    return slow