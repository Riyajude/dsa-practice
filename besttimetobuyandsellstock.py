class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0 

        min_price = prices[0]  
        max_profit = 0        

        for price in prices:
            if price < min_price:
                min_price = price 
            else:
                profit = price - min_price  
                max_profit = max(max_profit, profit)  

        return max_profit 
