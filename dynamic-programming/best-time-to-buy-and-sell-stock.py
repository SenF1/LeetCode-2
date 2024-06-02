class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buyPrice = prices[0]
        maxProfit = 0
        for price in prices[1:]:
            if price < buyPrice:
                buyPrice = price
            profit = price - buyPrice
            if profit > maxProfit: maxProfit = profit
        
        return maxProfit
            

