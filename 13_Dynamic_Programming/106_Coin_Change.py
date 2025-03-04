def coinChange(self, coins: List[int], amount: int) -> int:
    
    coins.sort()
    
    def dfs(target):
        
        if target == 0:
            return 0
        
        res = amount + 1
        
        for coin in coins:
           res = min(res, dfs(target - coin) + 1)
           
        return res
           
    ans = dfs(amount)
    
    if ans < amount + 1:
        return ans
    else:
        return -1
    
def coinChange2(self, coins: List[int], amount: int) -> int:
    
    # Create a cache, where cache[i] represents the min num of coins needed to sum to i
    # Initialize values to amount+1, which is impossible
    cache = [amount + 1] * (amount + 1)
    
    cache[0] = 0 # 0 coins needed to sum to 0
    
    for a in range(1, amount + 1):
        
        for c in coins:
            
            if (a - c) >= 0:
                
                cache[a] = min(cache[a], cache[a - c] + 1)
                
    if cache[amount] < amount + 1:
        return cache[amount]  
    else:
        return -1
                
        