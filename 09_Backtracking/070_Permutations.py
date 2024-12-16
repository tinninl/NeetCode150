def permute(nums: list[int])-> list[list[int]]:
    
    res = []
    
    def backtrack(tempList):
        
        if len(tempList) == len(nums):
            res.append(tempList.copy())
            
        else:
            
            for i in range(len(nums)):
                
                if nums[i] in tempList:
                    continue
                
                tempList.append(nums[i])
                backtrack(tempList)
                tempList.pop()
                
    backtrack([])
    
    return res

x = [1,2,3]
res = permute(x)
print(res)