"""
309. Best Time to Buy and Sell Stock with Cooldown

You are given an array prices where prices[i] is the price of a given stock on the ith day.

Find the maximum profit you can achieve. You may complete as many transactions as you like 
(i.e., buy one and sell one share of the stock multiple times) with the following restrictions:

After you sell your stock, you cannot buy stock on the next day (i.e., cooldown one day).
Note: You may not engage in multiple transactions simultaneously 
(i.e., you must sell the stock before you buy again).

Example 1:

Input: prices = [1,2,3,0,2]
Output: 3
Explanation: transactions = [buy, sell, cooldown, buy, sell]
Example 2:

Input: prices = [1]
Output: 0
 

Constraints:

1 <= prices.length <= 5000
0 <= prices[i] <= 1000
"""

class Solution:
    
    def maxProfit(self, prices: list[int]) -> int:
        
        if not prices:
            return 0
        
        n = len(prices)
        
        dp = [[0] * 3 for _ in range(n)]
        
        dp[0][0] = -prices[0]
        dp[0][1] = 0
        dp[0][2] = 0
        
        for i in range (1, n):
            
            # Holding a stock
            dp[i][0] = max(dp[i - 1][0], dp[i - 1][2] - prices[i])
            
            # In cooldown (sold stock previous day)
            dp[i][1] = dp[i - 1][0] + prices[i]
            
            # Not holding stock and not in cooldown
            dp[i][2] = max(dp[i - 1][2], dp[i - 1][1])
            
        return max(dp[-1][1], dp[-1][2])
    
    """
    There are three states on any given day:
    1. We currently have stock, having either bought the stock today or on a previous day
    2. We are in cooldown having sold today, so tmrw we can't buy stock
    3. We do not have a stock, having sold stock today
    """
    