# Need to use a hashset to meet the O(n) time requirement
# Trick: Which elements are the start of a sequence? 

class Solution:
    
    def longestConsecutiveSequence(nums: list[int]) -> int:
        
        numSet = set(nums)
        
        maxLength = 0
        
        for n in nums:
            
            # Identify which elements are the START of a sequence
            # x is the start of a sequence if x - 1 DNE
            if (n - 1) not in numSet:
                
                length = 1
                
                while (n + length) in numSet:
                    length += 1
                    
            maxLength = max(maxLength, length)
                
        return maxLength
                