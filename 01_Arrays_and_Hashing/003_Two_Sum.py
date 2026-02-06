# Use a hashmap to track both indices and elements

class Solution:
    
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        
        seen = {} # key = element, value = index
        
        for i, n in enumerate(nums):
            
            diff = target - n
            
            if diff in seen:
                
                return[seen.get(diff), i]
            
            seen[n] = i
      