def maxProfit(self, prices: List[int]) -> int:
    
    maxProfit = 0
    profit = 0
    
    buy = 0 # buy date
    sell = 1 # sell date
    
    while (sell < len(prices)):
        
        if (prices[sell] < prices[buy]):
            buy = sell
            
        else:
            profit = prices[sell] - prices[buy]
            maxProfit = max(profit, maxProfit)
            
        sell += 1
        
    return maxProfit