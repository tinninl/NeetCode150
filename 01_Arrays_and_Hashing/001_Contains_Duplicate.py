# Use a hashset to track seen elements.
# If the element exists in the set, then we've found the duplicate
class Solution:
    
    def containsDuplicate(self, nums: list[int]) -> bool:
        
        seen = set() # Initialize an empty hash set to track seen elements
        
        for n in nums: # Iterate through the array
            
            # If the element is already in the hash set, a duplicate exists
            if n in seen:
                return True
            
            # Add the element to the hash set
            seen.add(n)
        
        # No duplicates found
        return False