public class BestTimeToBuyAndSellStock {
    
    public int maxProfit(int[] prices){

        int maxProfit = 0, profit = 0;

        int buy = 0, sell = 1;  // days on which to buy and sell, respectively

        if (prices.length < 2)  
            return 0;

        while (sell < prices.length){

            if (prices[sell] < prices[buy]){

                buy = sell;  

            }

            else{

                profit = prices[sell] - prices[buy];
                maxProfit = Math.max(profit, maxProfit);
                
            }

            sell++;

        }

        return maxProfit;

    }

}
