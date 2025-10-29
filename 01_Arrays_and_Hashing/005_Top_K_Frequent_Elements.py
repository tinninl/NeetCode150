"""
Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

 

Example 1:

Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]
Example 2:

Input: nums = [1], k = 1
Output: [1]
 

Constraints:

1 <= nums.length <= 105
-104 <= nums[i] <= 104
k is in the range [1, the number of unique elements in the array].
It is guaranteed that the answer is unique.
 

Follow up: Your algorithm's time complexity must be better than O(n log n), where n is the array's size.
"""

def topKFrequent(self, nums: list[int], k: int) -> list[int]:
    
    count = {} # key = element, value = frequency
    
    # If there are 6 elements in nums, then freq must be of size 7, to represent
    # frequencies 0-6
    freq = [[] for i in range(len(nums) + 1)] # index = frequency
    
    for n in nums:
        count[n] = 1 + count.get(n, 0)
        
    for n, c in count.items():
        freq[c].append(n)
        
    res = []
    
    for i in range(len(freq) - 1, 0, -1):
        
        res += freq[i] # if the bucket is empty, thats ok, len(res) wont change
        
        if len(res) == k:
            return res
            
    # O(n)