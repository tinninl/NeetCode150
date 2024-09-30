def maxProfit(self, prices: List[int]) -> int:
    
    maxProfit = 0
    profit = 0
    
    l = 0
    r = 1
    
    while (r < len(prices)):
        
        if (prices[r] < prices[l]):
            l = r
            
        else:
            profit = prices[r] - prices[l]
            maxProfit = max(profit, maxProfit)
            
        r += 1
        
    return maxProfit