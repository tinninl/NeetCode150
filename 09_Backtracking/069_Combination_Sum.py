class Solution:
    
    def combinationSum(candidates: list[int], target: int) -> list[list[int]]:
        
        res= []
        
        def dfs(start, tempList, remain):
            
            if remain < 0:
                return
            
            if remain == 0:
                res.append(tempList.copy())
                return
            
            for i in range(start, len(candidates)):
                tempList.append(candidates[i])
                dfs(i, tempList, remain - candidates[i])
                tempList.pop()
            
            
        dfs(0, [], target)
        
        return res
    
x = [2,3,6,7]

res = Solution.combinationSum(x, 7)

print(res)