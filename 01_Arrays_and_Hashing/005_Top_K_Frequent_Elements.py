# Use a hashmap to track the frequencies of each number in the array
# The trick is to somehow sort the hashmap to get the top k most freq elements
#

class Solution:
    
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        
        # 1. Count the number of each element 
        count = {}  # Key = element, Value = count
        
        for num in nums:
            if num in count:
                count[num] += 1
            else:
                count[num] = 1
        
        # 2. Create buckets for each frequency
        # For an array of length x, we will need x+1 buckets.
        # Ex. For an array of length 6, we need 7 buckets to represent frequencies of 0-6
        frequencies = [[] for i in range(len(nums) + 1)] # index = frequency
        
        for num, c in count.items():
            frequencies[c].append(num)
            
        # Create result, the top k highest frequencies
        res = []
        
        for i in range(len(frequencies) - 1, 0, -1):
            
            res += frequencies[i] # if the bucket is empty, thats ok, len(res) wont change
            
            if len(res) == k:
                return res
                
        # O(n)