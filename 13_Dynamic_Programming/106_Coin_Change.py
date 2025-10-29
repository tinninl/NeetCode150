"""
322. Coin Change

You are given an integer array coins representing coins of different denominations 
and an integer amount representing a total amount of money.

Return the fewest number of coins that you need to make up that amount. 
If that amount of money cannot be made up by any combination of the coins, return -1.

You may assume that you have an infinite number of each kind of coin.

Example 1:

Input: coins = [1,2,5], amount = 11
Output: 3
Explanation: 11 = 5 + 5 + 1
Example 2:

Input: coins = [2], amount = 3
Output: -1
Example 3:

Input: coins = [1], amount = 0
Output: 0

Constraints:

1 <= coins.length <= 12
1 <= coins[i] <= 231 - 1
0 <= amount <= 104
"""

"""
Step One: What is the subproblem?
If i have a 5 coin and my target is 7, i need to know coinchange[2]

Step Two: What is the state?
Let dp[i] = min number of coins to reach i

Step Three: What is the recurrence relation?
dp[i] = min(dp[i] dp[i

Step Four: Base case
dp[0] = 0
"""
class Solution:
    def coinChange(self, coins: list[int], amount: int) -> int:
        # Initialize dp array with -1 to indicate that no amount has been computed yet.
        dp = [-1] * (amount + 1)
        
        # Base case: 0 coins are needed to make amount 0.
        dp[0] = 0
        
        def dfs(i):
            # If the result for the current amount is already computed, return it.
            if dp[i] != -1:
                return dp[i]
            
            # Initialize the minimum coins as a large number (amount + 1).
            dp[i] = amount + 1
            
            # Try each coin
            for coin in coins:
                if i - coin >= 0:  # We only care about valid subproblems
                    dp[i] = min(dp[i], dfs(i - coin) + 1)
            
  
            return dp[i]
        
        # Call the dfs function for the target amount
        res = dfs(amount)
        
        # If res is still the initial value (amount + 1), return -1 as it's not possible to form the amount.
        return res if res != amount + 1 else -1

        
    def coinChangeTab(self, coins: list[int], amount: int) -> int:
        
        dp = [amount + 1] * (amount + 1) # 11 coins to make 10 is impossible
        
        # Base case: 0 coins needed to make 0
        dp[0] = 0 
        
        # Consider every amount
        for a in range(1, len(dp)):
            
            # Consider every coin
            for c in coins:
                
                # If the coin value is greater than the target amount, skip
                if (a - c) >= 0:
                    
                    dp[a] = min(dp[a], dp[a - c] + 1)
                    
        if dp[amount] < amount + 1:
            return dp[amount]  
        else:
            return -1
                    
            