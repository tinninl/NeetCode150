class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        
        res = []
        subset = []
        
        def backtrack(i: int):
            
            # reach end of array, add subset
            if i == len(nums):
                res.append(subset.copy())
                return
            
            for n in nums:
                subset.append(nums[i])
                backtrack(i + 1)
            
            # include
            subset.append(nums[i])
            backtrack(i + 1)
            #skip
            subset.pop()
            backtrack(i + 1)
            
        backtrack(0)
        
        return res
            
            
            
        
        
        
        